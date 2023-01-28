from hydraulic_catalog import *

# https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable

from json import JSONEncoder

def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default


t = Thread(Thread_3_8(), InnerThread())
s = json.dumps(t)
print(s)

