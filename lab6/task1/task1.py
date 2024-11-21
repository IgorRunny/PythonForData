from lxml import etree

xml_file = "ex_1.xml"
xml_error_file = "ex_1_error.xml"
xsd_file = "ex_1.xsd"

with open(xsd_file, 'r') as file:
    schema_root = etree.XML(file.read())

schema = etree.XMLSchema(schema_root)
xml_doc = etree.parse(xml_file)
xml_error_doc = etree.parse(xml_error_file)

try:
    schema.assertValid(xml_doc)
    print(f"File {xml_file} is valid to {xsd_file} schema")
except etree.DocumentInvalid as e:
    print(f"File {xml_file} is not valid to {xsd_file} schema")
    print("Error message:")
    print(e)

print()

try:
    schema.assertValid(xml_error_doc)
    print(f"File {xml_error_file} is valid to {xsd_file} schema")
except etree.DocumentInvalid as e:
    print(f"File{xml_error_file} is not valid to {xsd_file} schema")
    print("error message:")
    print(e)