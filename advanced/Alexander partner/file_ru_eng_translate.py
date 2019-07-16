import pandas as pd
import xlrd, xlwt

listEng = []
listChina = []

rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/ГЖ/eng_rus_partner_Alexander.xlsx',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
  row = sheet.row_values(rownum)
  listEng.append(row[0])
  listChina.append(row[1])

data = pd.Series(listChina, index=listEng)

listNewEng = []
listNewRus = []

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0, 0, "Русский")
sheet1.write(0, 1, "Английский")

i=0