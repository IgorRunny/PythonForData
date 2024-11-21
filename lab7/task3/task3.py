import json

json_file = 'ex_3.json'

with open(json_file, 'r') as file:
    json_doc = json.load(file)

new_invoice = json_doc['invoices'][-1].copy()
new_invoice['id'] = 3
new_invoice['items'] = new_invoice['items'].copy()

new_items = [
    {'name' : 'item4', 'quantity' : 3, 'price' : 35.00},
    {'name' : 'item5', 'quantity' : 6, 'price' : 400.00}
]

new_invoice['items'].extend(new_items)
new_invoice['total'] += sum(item['price'] * item['quantity'] for item in new_items)

json_doc['invoices'].append(new_invoice)

new_json_file = 'ex_3_new.json'
with open(new_json_file, 'w') as file:
    json.dump(json_doc, file, indent=2)