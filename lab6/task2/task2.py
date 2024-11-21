import xml.etree.ElementTree as ET

tree = ET.parse('ex_2_new.xml')
root = tree.getroot()

sum = 0
sum_rows = 0

for item in root.iter('Item'):
    sum_string = item.find('QNT').text.replace(',', '.')
    sum += float(sum_string)
    sum_rows += int(item.find('QNTRows').text)

summary = root.find('Summary')
summary[0].text = str(sum)
summary[1].text = str(sum_rows)

try:
    tree.write('ex_2_summary.xml', 'UTF-8')
    print('File ex_2_summary.xml was created')
except:
    print('Error into writing file ex_2_summary.xml')