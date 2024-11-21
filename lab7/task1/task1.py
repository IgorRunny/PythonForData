import json
from genson import SchemaBuilder
from jsonschema import validate

def validateJSON (json_doc, schema):
    try:
        validate(instance=json_doc, schema=schema)
        print('Valid json')
    except Exception as e:
        print('Invalid json')
        print(e)

json_file = 'ex_1.json'
json_error_file = 'ex_1_error.json'

with open(json_file, 'r') as file, open(json_error_file, 'r') as error_file:
    json_doc = json.load(file)
    json_error_doc = json.load(error_file)

builder = SchemaBuilder()
builder.add_schema({"type": "object", "properties": {}})
builder.add_object(json_doc)

with open('ex_1_schema.json', 'w') as schema_file:
    schema_file.write(builder.to_json(indent = 2))

schema = builder.to_schema()

validateJSON(json_doc, schema)

validateJSON(json_error_doc, schema)