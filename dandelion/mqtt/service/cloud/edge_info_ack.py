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

import json
from logging import LoggerAdapter
from typing import Any, Dict

import paho.mqtt.client as mqtt
from oslo_log import log
from sqlalchemy.orm import Session

from dandelion import crud
from dandelion.crud import utils as db_util
from dandelion.db import session
from dandelion.mqtt.server import get_mqtt_client
from dandelion.mqtt.service import RouterHandler
from dandelion.mqtt.topic.v2x_config import V2X_CONFIG_UPDATE_NOTICE

LOG: LoggerAdapter = log.getLogger(__name__)


class EdgeInfoACKRouterHandler(RouterHandler):
    def handler(self, client: mqtt.MQTT_CLIENT, topic: str, data: Dict[str, Any]) -> None:
        from dandelion.mqtt.cloud_server import set_edge_id

        node_id = int(data.get("id", 0))
        set_edge_id(node_id)
        db: Session = session.DB_SESSION_LOCAL()
        crud.system_config.update_node_id(db, _id=1, node_id=node_id)

        # Notification cerebrum
        get_mqtt_client().publish(topic=V2X_CONFIG_UPDATE_NOTICE, payload=json.dumps({}), qos=0)
        db_util.refresh_cloud_rsu(db)
