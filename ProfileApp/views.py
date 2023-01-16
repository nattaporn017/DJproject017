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
def showMydata(request):
    name="Nattaporn"
    surname="Boonmala"
    gender="women"
    status="student"
    work="RMUTI"
    education="BIS"
    context = {'name':name, 'surname':surname, 'gender':gender, 'status':status, 'work':work, 'education':education}
    return render(request, 'showMydata.html',context)
    # return render(request, 'showMydata.html',
    # {'name':name, 'surname':surname, 'gender':gender, 'status':status, 'work':work, 'education':education})







# def head(request):
#     return render(request,'header.html')
# def menu(request):
#     return render(request,'menu.html')
# def base(request):
#     return render(request,'base.html')