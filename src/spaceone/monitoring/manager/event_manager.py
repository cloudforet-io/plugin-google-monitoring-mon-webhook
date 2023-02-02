import logging
import hashlib
import json
from spaceone.core import utils
from datetime import datetime
from spaceone.core.manager import BaseManager
from spaceone.monitoring.manager.incident_1_2 import Incident_1_2
from spaceone.monitoring.manager.incident import Incident

from spaceone.monitoring.model.event_response_model import EventModel
from spaceone.monitoring.error.event import *
_LOGGER = logging.getLogger(__name__)
_EXCEPTION_TO_PASS = ["Test notification"]


class EventManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, raw_data):
        results = []

        version = raw_data.get('version')
        if version == '1.2':
            inst = Incident_1_2(raw_data.get('incident', {}), version)
        elif version == 'test':
            inst = Incident(raw_data.get('incident', {}), version)
        else:
            # unsupported version
            inst = Incident(raw_data.get('incident', {}), version)
            _LOGGER.critical(f'Unsupported version: {version}')
        event_dict = inst.get_event_dict()
        event_vo = self._check_validity(event_dict)
        results.append(event_vo)
        _LOGGER.debug(f'[EventManager] parse Event : {event_dict}')

        return results

    @staticmethod
    def _check_validity(event_dict):
        try:
            event_result_model = EventModel(event_dict, strict=False)
            event_result_model.validate()
            event_result_model_primitive = event_result_model.to_native()
            return event_result_model_primitive

        except Exception as e:
            raise ERROR_CHECK_VALIDITY(field=e)

