"""
JSON Override classes for Gearman clients and workers
"""

import json
import decimal
import gearman

class _JSONEncoder(json.JSONEncoder):
    """
    Override JSON encoder class that recognizes decimals
    """
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(_JSONEncoder, self).default(obj)

class _JSONDataEncoder(gearman.DataEncoder):
    """
    Override Gearman DataEncoder class to send/receive JSON data
    """
    @classmethod
    def encode(cls, encodable_object):
        return json.dumps(encodable_object, cls=_JSONEncoder)
    @classmethod
    def decode(cls, decodable_string):
        return json.loads(decodable_string)

class GearmanWorker(gearman.GearmanWorker):
    data_encoder = _JSONDataEncoder
    def after_poll(self, any_activity):
        return True

class GearmanClient(gearman.GearmanClient):
    data_encoder = _JSONDataEncoder
