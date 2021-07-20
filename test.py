import xlrd
file=r'D:\djangoProject\grade.xlsx'
data=xlrd.open_workbook(file)
table=data.sheets()[0]
print(data.sheet_names())
nrows=table.nrows
ncols=table.ncols
for rn in range(table.nrows):
    print (table.row_values(rn))
row_title=table.row_values(0, start_colx=0, end_colx=19)
print(row_title)
col_id=table.col_values(2, start_rowx=1, end_rowx=19)
print(col_id)
col_password=table.col_values(3,start_rowx=1,end_rowx=19)
print(col_password)
test_id='001'
test_pwd='123'
index=1
for i in col_id:
    # print(test_id)
    # print(i)
    if test_id==i and test_pwd==table.cell_value(index,3):
        print(table.row_values(index, start_colx=4, end_colx=19))
        break
    else:
        print('验证失败')
    index = index + 1
