"""
GearmanWorker and GearmanClient classes that send/receive data in JSON format.

Please note that the default python json encoder has been extended to also
encode Decimal data.
"""

import json
import decimal
import gearman

class _JSONEncoder(json.JSONEncoder):
    """
    An override JSON encoder class that recognizes Decimal objects.
    """
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(_JSONEncoder, self).default(obj)

class _JSONDataEncoder(gearman.DataEncoder):
    """
    An override Gearman DataEncoder class to send/receive JSON data.
    """
    @classmethod
    def encode(cls, encodable_object):
        return json.dumps(encodable_object, cls=_JSONEncoder)
    @classmethod
    def decode(cls, decodable_string):
        return json.loads(decodable_string)

class GearmanWorker(gearman.GearmanWorker):
    """
    Extend gearman.GearmanWorker to receive job data in JSON format.
    """
    data_encoder = _JSONDataEncoder
    def after_poll(self, any_activity):
        return True

class GearmanClient(gearman.GearmanClient):
    """
    Extend gearman.GearmanClient to send job data in JSON format.
    """
    data_encoder = _JSONDataEncoder
