from openpyxl import Workbook

data = [
    {"Таб. номер": "0002", "Фамилия": "Петров П.П.", "Отдел": "Бухгалтерия", "Сумма по окладу, руб.": 3913.04, "Сумма по надбавкам, руб.": 2608.7, "Сумма зарплаты, руб.": 6521.74, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Таб. номер": "0005", "Фамилия": "Васин В.В.", "Отдел": "Бухгалтерия", "Сумма по окладу, руб.": 5934.78, "Сумма по надбавкам, руб.": 913.04, "Сумма зарплаты, руб.": 6847.83, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Итог": "Бухгалтерия"},
    {"Таб. номер": "0003", "Фамилия": "Иванов И.И.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 6000.00, "Сумма по надбавкам, руб.": 4000.00, "Сумма зарплаты, руб.": 10000.00, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Таб. номер": "0006", "Фамилия": "Сидоров С.С.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 5000.00, "Сумма по надбавкам, руб.": 4500.00, "Сумма зарплаты, руб.": 9500.00, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Таб. номер": "0008", "Фамилия": "Петров Л.И.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 4074.07, "Сумма по надбавкам, руб.": 2444.44, "Сумма зарплаты, руб.": 6518.52, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Таб. номер": "0007", "Фамилия": "Волков В.В.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 1434.78, "Сумма по надбавкам, руб.": 1434.78, "Сумма зарплаты, руб.": 2869.57, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Итог": "Отдел кадров"},
    {"Таб. номер": "0004", "Фамилия": "Мишин М.М.", "Отдел": "Столовая", "Сумма по окладу, руб.": 5500.00, "Сумма по надбавкам, руб.": 3500.00, "Сумма зарплаты, руб.": 9000.00, "НДФЛ, %": 13, "Сумма НДФЛ, руб.": "", "Сумма к выдаче, руб.": ""},
    {"Итог": "Столовая"},
    {"Общий итог": "Общий итог"}
]

workbook = Workbook()
sheet = workbook.active

headers = data[0].keys()
sheet.append(list(headers))

department_salary_sum = 0
department_allowance_sum = 0
department_total_pay_sum = 0
department_ndfl_sum = 0
department_net_pay_sum = 0

total_salary_sum = 0
total_allowance_sum = 0
total_total_pay_sum = 0
total_ndfl_sum = 0
total_net_pay_sum = 0

for row in data:
    if "Итог" in row.keys():
        sheet.append(list(["", "", row['Итог'] + " Итог", department_salary_sum, department_allowance_sum, department_total_pay_sum, "", department_ndfl_sum, department_net_pay_sum]))
        total_salary_sum += department_salary_sum
        total_allowance_sum += department_allowance_sum
        total_total_pay_sum += department_total_pay_sum
        total_ndfl_sum += department_ndfl_sum
        total_net_pay_sum += department_net_pay_sum
        department_salary_sum = 0
        department_allowance_sum = 0
        department_total_pay_sum = 0
        department_ndfl_sum = 0
        department_net_pay_sum = 0
    elif "Общий итог" in row.keys():
        sheet.append(list(["", "", row['Общий итог'], total_salary_sum, total_allowance_sum, total_total_pay_sum, "", total_ndfl_sum, total_net_pay_sum]))
    else:
        row['Сумма НДФЛ, руб.'] = round(row['Сумма зарплаты, руб.'] * row['НДФЛ, %'] / 100, 2)
        row["Сумма к выдаче, руб."] = row["Сумма зарплаты, руб."] - row["Сумма НДФЛ, руб."]
        department_salary_sum += row["Сумма по окладу, руб."]
        department_allowance_sum += row["Сумма по надбавкам, руб."]
        department_total_pay_sum += row["Сумма зарплаты, руб."]
        department_net_pay_sum += row["Сумма к выдаче, руб."]
        department_ndfl_sum += row["Сумма НДФЛ, руб."]
        sheet.append(list(row.values()))

workbook.save("table.xlsx")