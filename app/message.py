import json
import logging

logging.basicConfig(level=logging.INFO)


class Format:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def to_json(self):
        return json.dumps({"key": self.key, "value": self.value})
    
    @staticmethod
    def from_json(data):
        try:
            v = json.loads(data)
            return Format(v["key"], v["value"])
        except Exception as exc:
            logging.error(f"Deserialization error: {exc}")
            return None
