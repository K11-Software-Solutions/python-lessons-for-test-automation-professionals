import json

with open('myjson.json') as json_file:
    json_string = json_file.read()
    data = json.loads(json_string)
    for item in data:
        print(item,':',data[item])