from django.http import HttpResponse
from django.shortcuts import render
# 表单
def search_form(request):
    return render(request, 'search_form.html')
# 接收请求数据
list=[]
flag=False
name=''
def search(request):
    request.encoding = 'utf-8'
    userID=request.GET['userid']
    pwd=request.GET['pwd']
    flag=VerifyID(userID,pwd)
    total=list[0]
    score=list[1]
    rank=list[2]
    mzd=list[3]
    xjp=list[4]
    qrs=list[5]
    qrs_ex=list[6]
    eng=list[7]
    pe=list[8]
    os=list[9]
    algo=list[10]
    algo_ex=list[11]
    matlab=list[12]
    os_ex=list[13]
    xs=list[14]
    if flag:
        data={
            "id":userID,
            "pwd":pwd,
            "name":name,
            "total":total,
            "score":score,
            "rank":rank,
            "mzd":mzd,
            "xjp":xjp,
            "qrs":qrs,
            "qrs_ex":qrs_ex,
            "eng":eng,
            "pe":pe,
            "os":os,
            "algo":algo,
            "algo_ex":algo_ex,
            "matlab":matlab,
            "os_ex":os_ex,
            "xs":xs
        }
        return render(request,"grade.html",{
            "userid":data['id'],
            "name":data['name'],
            "total":data['total'],
            "score":data['score'],
            "rank":data['rank'],
            "mzd":data['mzd'],
            "xjp":data['xjp'],
            "qrs":data['qrs'],
            "qrs_ex":data['qrs_ex'],
            "eng":data['eng'],
            "pe":data['pe'],
            "os":data['os'],
            "algo":data['algo'],
            "algo_ex":data['algo_ex'],
            "matlab":data['matlab'],
            "os_ex":data['os_ex'],
            "xs":data['xs']
            })
    else:
        message='未查询到相关信息，请您联系系统管理员！谢谢！！！'
        return render(request,"error.html", {'message':message})

def VerifyID(id, password):
    import xlrd
    file = r'D:\djangoProject\grade.xlsx'
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    print(data.sheet_names())
    nrows = table.nrows
    ncols = table.ncols
    for rn in range(table.nrows):
        print(table.row_values(rn))
    row_title = table.row_values(0, start_colx=0, end_colx=19)
    print(row_title)
    col_id = table.col_values(2, start_rowx=1, end_rowx=19)
    print(col_id)
    col_password = table.col_values(3, start_rowx=1, end_rowx=19)
    print(col_password)
    index = 1
    for i in col_id:
        if id == i and password == table.cell_value(index, 3):
            global list
            global name
            list = table.row_values(index, start_colx=4, end_colx=19)
            name=table.cell_value(index,1)
            flag = True
            break
        else:
            flag=False
        index = index + 1
    return flag


