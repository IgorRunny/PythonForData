from docx import Document


doc = Document('file.docx')
table = doc.tables[0]
Dict = {}
for row in table.rows[1:]:
    key = row.cells[0].text
    value = row.cells[2].text
    Dict[key] = value
print(Dict)