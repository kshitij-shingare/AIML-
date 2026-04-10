# JSON Module
#  import json
#  JSON - javascript object Notation

# json modules - 
        # 1) json.loads() - json string convert to python object
        # 2)json .dumps() - python object to json string
import json 
json_str = '{"name":"KBS","learning":true}'

pyth_obj = json.loads(json_str)

print(type(pyth_obj),pyth_obj)