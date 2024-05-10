import openpyxl # Для записи данных в Excell таблицу
import numpy as np # Для работы с матрицами

# Запись значений напряжений узловых потенциалов в файл U.xlsx
def U():
    wb = openpyxl.Workbook()
    sheet = wb.active
    c1 = sheet['B2']
    c1.value = 1.5
    wb.save("excell_tables\\U.xlsx")

U()