from openpyxl import load_workbook

file_path = "table.xlsx"
workbook = load_workbook(file_path)
sheet = workbook.active

sheet["B14"] = "максимальная зарплата"
sheet["B15"] = "минимальная зарплата"
sheet["B16"] = "средняя зарплата отделов по порядку:"

max_salary = sheet[2][5].value
min_salary = sheet[2][5].value
max_salary_index = 2
min_salary_index = 2

department_salary_sum = 0
department_sums = []

for row_index in range(2, 11):
    if row_index not in (4, 9):
        department_salary_sum += sheet[row_index][5].value
        if max_salary < sheet[row_index][5].value:
            max_salary_index = row_index
            max_salary = sheet[row_index][5].value
        if min_salary > sheet[row_index][5].value:
            min_salary_index = row_index
            min_salary = sheet[row_index][5].value
    else:
        department_sums.append(department_salary_sum)
        department_salary_sum = 0

department_sums.append(department_salary_sum)

employee_with_max_salary = sheet[max_salary_index][1].value
employee_with_min_salary = sheet[min_salary_index][1].value

department_sums[0] /= 2
department_sums[1] /= 4
department_sums[2] /= 1

sheet["C14"] = f"{employee_with_max_salary} - {max_salary}"
sheet["C15"] = f"{employee_with_min_salary} - {min_salary}"
sheet["C16"] = f"{department_sums[0]}, {department_sums[1]}, {department_sums[2]}"

workbook.save("table.xlsx")