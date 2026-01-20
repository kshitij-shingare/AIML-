import json 
json_str = '{"name":"KBS","learning":true}'

pyth_obj = json.loads(json_str)

print(type(pyth_obj),pyth_obj)