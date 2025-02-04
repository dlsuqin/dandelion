# Copyright 2022 99Cloud, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from logging import LoggerAdapter
from typing import Any, Dict

import paho.mqtt.client as mqtt
from oslo_log import log
from sqlalchemy.orm import Session

from dandelion import crud, schemas
from dandelion.db import session
from dandelion.mqtt.service import RouterHandler

LOG: LoggerAdapter = log.getLogger(__name__)


class EdgeRSUAddRouterHandler(RouterHandler):
    def handler(self, client: mqtt.MQTT_CLIENT, topic: str, data: Dict[str, Any]) -> None:
        LOG.info(f"{topic} => Edge RSU add {data}")
        db: Session = session.DB_SESSION_LOCAL()
        id_ = data.get("id")
        if id_ is not None:
            node_rsu = data.get("rsu")
            if node_rsu is not None:
                edge_node_rsu = schemas.EdgeNodeRSUCreate()
                edge_node_rsu.edge_node_id = id_
                edge_node_rsu.name = node_rsu.get("name", "")
                edge_node_rsu.esn = node_rsu.get("esn", "")
                edge_node_rsu.area_code = node_rsu.get("areaCode", "")
                location = node_rsu.get("location", {})
                if location is not None:
                    edge_node_rsu.location = schemas.Location()
                    edge_node_rsu.location.lon = location.get("lon", 0)
                    edge_node_rsu.location.lat = location.get("lat", 0)
                _ = crud.edge_node_rsu.create(db, obj_in=edge_node_rsu)
            LOG.info(f"{topic} => Edge RSU added")
