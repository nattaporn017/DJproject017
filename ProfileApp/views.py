from django.shortcuts import render,HttpResponse,redirect
import datetime

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


# lstOurProduct = []
#
# def listPro11(request):
#     products = "Supplementary Food"
#     name = "Nattaporn Boonmala"
#     date = datetime.datetime.now()
#     context = {'lstProduct': lstOurProduct,'products': products,'name': name,'date': date.strftime("%A %d-%m-%Y %H : %M")}
#     return render(request, 'listPro11.html', context)
#
# from ProfileApp.forms import *
# def inputPro11(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             brand = form.cleaned_data['brand']
#             type = form.cleaned_data['type']
#             price = form.cleaned_data['price']
#             delivery = form.cleaned_data['delivery']
#             amount = form.cleaned_data['amount']
#             productnew = Product(name, brand, type, price, delivery, amount)
#             lstOurProduct.append(productnew)
#             return redirect('listPro11')
#         else:
#             return redirect('pro_retrive_all')
#     else:
#         form = ProductForm()
#     context = {'form': form}
#     return render(request, 'inputPro11.html', context)



# from ProfileApp.models import *
# productslist=[]
# def showProducts(request):
#     # products = Product('P001','Moues','Acer',500.00,120)
#     # productslist.append(products)
#     # products = Product('P002', 'Case', 'HP', 1500.00, 100)
#     # productslist.append(products)
#     # products = Product('P003', 'Notebook', 'Acer', 18000.00, 80)
#     # productslist.append(products)
#     # products = Product('P004', 'Notebook', 'Asus', 20000.00, 65)
#     # productslist.append(products)
#     context = {'products':productslist}
#     return render(request,'showOurProducts.html',context)
#
# # def newProduct(request):
# #     if request.method == 'POST': #ซับมิทข้อมูลมาจากฟอร์ม
# #         id = request.POST['id']#อ่านค่า
# #         name = request.POST['name']
# #         brand = request.POST['brand']
# #         price = request.POST['price']
# #         net = request.POST['net']
# #         product = Product(id,name,brand,price,net)
# #         productslist.append(product)
# #         return redirect('showOur')
# #     else:
# #         return render(request,'frmProductNormal.html')
#
#
#
# from ProfileApp.forms import *
# def frmProduct(request):
#     if request.method == 'POST': #ซับมิทข้อมูลมาจากฟอร์ม
#         form = ProductFrom(request.POST)
#         if form.is_valid():
#             form = form.cleaned_data
#             id = form.get('id')
#             name = form.get('name')
#             brand = form.get('brand')
#             price = form.get('price')
#             net = form.get('net')
#             product = Product(id, name, brand, price, net)
#             productslist.append(product)
#             return redirect('showOur')
#     else:
#         form = ProductFrom()
#         context ={'form':form}
#         return render(request,'frmProduct.html',context)



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