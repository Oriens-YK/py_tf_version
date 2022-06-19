import numpy as np
import json
import re
# [[1,2,2,3],[2,2,2,3],[3,2,2,3]]
arr = []

arr.append(18168415)
arr.append(2186168)
dict1 = {'a':arr}
# dict to json
jsonStr  = json.dumps(dict1)
print(dict1)
print(jsonStr)
# json to dict
dict1 = json.loads(jsonStr)
print(dict1['a'], type(dict1['a']))
print(dict1['a'][0])