# -*- coding: utf-8 -*-
import json
from bson import json_util
from operator import eq

# json.dumps(anObject, default=json_util.default)
j1 = open('mongodb_json1.log', 'rb').read().decode("utf8")
j1 = json.loads(j1, object_hook=json_util.object_hook)

j2 = open('mongodb_json2.log', 'rb').read().decode("utf8")
j2 = json.loads(j2, object_hook=json_util.object_hook)

# print(sorted(j1.items(), key= lambda x:x[0]))
# print(sorted(j2.items(), key= lambda x:x[0]))
print(j1)
print( j1 == j2)
