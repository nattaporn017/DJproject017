from django.urls import path
from django.http import  HttpResponse
from ProfileApp import views

urlpatterns = [
    path('ass9', views.ass9, name = 'ass9'),
    path('info', views.info, name = 'info'),
    path('edu', views.edu, name = 'edu'),
    path('fav', views.fav, name = 'fav'),
    path('prod', views.prod, name = 'prod'),
    path('prod1', views.prod1, name = 'prod1'),
    path('prod2', views.prod2, name = 'prod2'),
    path('prod3', views.prod3, name = 'prod3'),
    path('prod4', views.prod4, name = 'prod4'),
    path('prod5', views.prod5, name = 'prod5'),
    path('prod6', views.prod6, name = 'prod6'),
    path('prod7', views.prod7, name = 'prod7'),
    path('prod8', views.prod8, name = 'prod8'),
    path('idol', views.idol, name = 'idol'),
    path('ass12', views.ass12, name = 'ass12'),
    path('showdatas', views.datas, name = 'showdatas'),
    path('listProduct', views.listProduct, name ='listProduct'),
    path('inputProduct', views.inputProduct, name='inputProduct'),

    path('retrieveAllProduct', views.retrieveAllProduct, name = 'retrieveAllProduct'),
    path('<pid>/retivevOneProduct', views.retivevOneProduct,name = 'retivevOneProduct'),

    path('createProduct', views.createProduct, name = 'createProduct'),
    # path('emp_create', views.emp_create, name='emp_create'),

    # path('showOur', views.showProducts, name = 'showOur'),
    # path('newProduct', views.newProduct, name = 'newProduct'),
    # path('frmProduct', views.frmProduct, name = 'frmProduct'),


    # path('head', views.head, name = 'head'),
    # path('menu', views.menu, name = 'menu'),
    # path('base', views.base, name = 'base'),
    path('showGoodsList', views.showGoodsList, name='showGoodsList'),
    path('<gid>/showGoodsOne', views.showGoodsOne, name='showGoodsOne'),
    path('newGoodsCreate', views.newGoodsCreate, name='newGoodsCreate'),
    path('<str:gid>/updateGoods', views.updateGood, name='updateGoods'),
    path('<str:gid>/goodsDel', views.deleteGoods, name='goodsDel'),
    path('showCustomerList', views.showCustomerList, name='showCustomerList'),
    path('<cid>/showCustomerOne', views.showCustomerOne, name='showCustomerOne'),
    path('newCustomerCreate', views.newCustomerCreate, name='newCustomerCreate'),
    path('<str:cid>/updateCustomer', views.updateCustomer, name='updateCustomer'),
    path('<str:cid>/cusDel', views.deleteCustomer, name='cusDel'),


    path('<pid>/updateProduct', views.updateProduct, name='updateProduct'),
    path('<pid>/deleteProductOld', views.deleteProductOld, name='deleteProductOld'),
    # path('<pid>/deleteProduct', views.deleteProduct, name='deleteProduct'),
]