from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
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
def ass12(request):
    return render(request,'ASS12/Assignment12.html')
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


lstOurProduct = []
# pd1 = product("P01", "รองเท้า adidas", "White", "36", 1499, 1, True)
# lstOurProduct.append(pd1)
def listProduct(request):
    details = "Wireless Headphones"
    name = "Nattaporn Boonmala"
    date = datetime.datetime.now()
    return render(request, 'Ass11/listPro11.html', {'lstProduct': lstOurProduct,
                                              'details': details, 'name': name,
                                              'date': date.strftime("%A %d-%m-%Y %H : %M")})
def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm11(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            pattern = form.cleaned_data['pattern']
            color = form.cleaned_data['color']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            delivery = form.cleaned_data['delivery']
            productNew = product11(id, name, pattern, color, price, amount,delivery)
            lstOurProduct.append(productNew)
            return redirect('listProduct')
        else:
            return redirect('pro_retrive_all')
    else:
        form = ProductForm11()
    context = {'form': form}
    return render(request, 'Ass11/inputPro11.html', context)


from .models import *
from ProfileApp.forms import *
def retrieveAllProduct(request):
    products = Product.objects.all() #อ่ํานข้อมูลทุกเรคอร์ด All ในฐํานข้อมูลที่เชื่อมโดย Category
    context ={'products':products}
    return render(request, 'Product/retrieveAllProduct.html',context)

def retivevOneProduct(request, pid):
    product = Product.objects.get(pid=pid) #อ่ํานข้อมูลทุกเรคอร์ด One ในฐํานข้อมูลที่เชื่อมโดย Category
    context ={'product':product}
    return render(request, 'Product/retivevOneProduct.html',context)

from django.contrib import messages

def createProduct(request):
    if request.method == 'POST':
        form = ProductMForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกข้อมูลสินค้าใหม่เรียบร้อย...')
            return redirect('retrieveAllProduct')
        else:
            product = Product.objects.get(pid=request.POST['pid'])
            if product:
                messages.add_message(request,messages.WARNING,'รหัสสินค้าซ้ำกับที่มีอยู่แล้วในระบบ')
            messages.add_message(request, messages.WARNING,'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้')
    else:
        form = ProductMForm()
    context = {'form':form}
    return render(request, 'Product/createProduct.html',context)
def updateProduct (request,pid):
    product = get_object_or_404(Product, pid=pid)
    form = ProductMForm(data=request.POST or None,instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขข้อมูลสินค้าเรียบร้อย...')
            return redirect('retrieveAllProduct')
        else:
            context = {'form': form}
            messages.add_message(request, messages.WARNING, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้')
    else:
        form.up
        context = {'form':form}
        # context = {'form': form, 'old_pid': product.pid}

        return  render(request, 'Product/updateProduct.html',context)
def deleteProductOld (request,pid):
    product = get_object_or_404(Product, pid=pid)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลสินค้าเรียบร้อย...')
    else:
        messages.add_message(request, messages.WARNING, 'ไม่สามารถลบข้อมูลสินค้า ตามรหัสที่ระบุได้ ')
    return redirect('retrieveAllProduct')
# def deleteProduct (request,pid=None):
#     if request.method == 'POST':
#         pid = request.POST['pid']
#         product = Product.objects.get(pid=pid)
#         product.delete()
#         return redirect('retrieveAllProduct')
#     else:
#         product = Product.objects.get(pid=pid)
#         context = {'product': product}
#         return render(request, 'Product/deleteProduct.html', context)





#######งาน12
def showGoodsList (request):
    #Query
    result = Goods12.objects.all()
    context ={'result' : result}
    return render(request, 'ASS12/showGoodsList.html', context)

def showGoodsOne (request,gid):
    goodsone_info = Goods12.objects.get(gid=gid)
    context= {'goods': goodsone_info}
    return render(request, 'ASS12/showGoodsOne.html', context)
def showCustomerList (request):
    result = Customer12.objects.all()
    context = {'result': result }
    return render(request, 'ASS12/showCustomerList.html', context)
def showCustomerOne (request,cid):
    customerone_info = Customer12.objects.get(cid=cid)
    context={'customer':customerone_info}
    return render(request, 'ASS12/showCustomerOne.html', context)