from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request,'infoSTD.html')
def edu(request):
    return render(request,'eduSTD.html')
def fav(request):
    return render(request,'favorites.html')
def prod(request):
    return render(request,'products.html')
def prod1(request):
    return render(request,'prod1.html')
def prod2(request):
    return render(request,'prod2.html')
def prod3(request):
    return render(request,'prod3.html')
def prod4(request):
    return render(request,'prod4.html')
def prod5(request):
    return render(request,'prod5.html')
def prod6(request):
    return render(request,'prod6.html')
def prod7(request):
    return render(request,'prod7.html')
def prod8(request):
    return render(request,'prod8.html')
def idol(request):
    return render(request,'idol.html')

def datas(request):
    name="Nattaporn"
    surname="Boonmala"
    gender="Women"
    homeland="Chonbure"
    weight="46"
    color="Pink"
    job= "Cashier"
    idStd= " 65342310017-1"
    address= "Khonkaen"
    height= "154"
    food= "Salad"
    prolist = [["นมหมีรสชาเขียว", "18.00", 'images/milk1.jpg'],
                          ["นมหมีรสงาขาว", "18.00", 'images/milk2.jpg'],
                          ["นมหมีรสไวท์มอล", "18.00", 'images/milk3.jpg'],
                          ["นมหมีรสเชอร์รี่", "18.00", 'images/milk4.jpg'],
                          ["นมหมีรสโกจิเบอร์รี่", "18.00", 'images/milk5.jpg'],
                          ["นมหมี Hight folate", "15.00", 'images/milk6.jpg'],
                          ["นมหมีรส Low Fa", "15.00", 'images/milk7.jpg'],
                          ["นมหมีรส 0% Fat", "15.00", 'images/milk8.jpg'],
                          ["นมหมีรสออริจินัล", "15.00", 'images/milk9.jpg'],
                          ["นมหมีรสจืด", "76.00", 'images/milk10.jpg'],]
    context = {'name': name, 'surname': surname, 'gender': gender,
               'homeland': homeland, 'weight': weight, 'color': color,
               'job': job, 'idStd': idStd, 'address': address, 'height': height, 'food': food, 'lists':prolist}
    return render(request, 'datas.html',context)

# def datasPro(request):
#     prolist=["นมหมีรสชาเขียว","นมหมีรสงาขาว","นมหมีรสไวท์มอล์","นมหมีรสเชอร์รี่","นมหมีรสโกจิเบอร์รี่",
#              "นมหมี Hight folate","นมหมีรส Low Fat","นมหมีรส 0% Fat","นมหมีรสออริจินัล","นมหมีรสจืด",]
#     return render(request, 'datas.html',prolist)







# def head(request):
#     return render(request,'header.html')
# def menu(request):
#     return render(request,'menu.html')
# def base(request):
#     return render(request,'base.html')