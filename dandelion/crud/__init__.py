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

from .crud_area import area
from .crud_camera import camera
from .crud_city import city
from .crud_country import country
from .crud_map import map
from .crud_map_rsu import map_rsu
from .crud_mng import mng
from .crud_province import province
from .crud_radar import radar
from .crud_rsi_event import rsi_event
from .crud_rsm import rsm
from .crud_rsm_participant import rsm_participant
from .crud_rsu import rsu
from .crud_rsu_config import rsu_config
from .crud_rsu_config_rsu import rsu_config_rsu
from .crud_rsu_log import rsu_log
from .crud_rsu_model import rsu_model
from .crud_rsu_query import rsu_query
from .crud_rsu_query_result import rsu_query_result
from .crud_rsu_tmp import rsu_tmp
from .crud_system_config import system_config
from .crud_user import user

__all__ = [
    "user",
    "country",
    "area",
    "city",
    "province",
    "rsu",
    "rsu_tmp",
    "rsu_model",
    "rsu_config",
    "radar",
    "rsu_log",
    "camera",
    "map",
    "map_rsu",
    "mng",
    "rsi_event",
    "rsm_participant",
    "rsu_query",
    "rsu_query_result",
    "rsm",
    "rsu_config_rsu",
    "system_config",
]
