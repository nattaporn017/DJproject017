from django.db import models
class product11():
    def __init__(self,id, name, pattern, color, price, amount,delivery):
        self.__id = id
        self.__name = name
        self.__pattern = pattern
        self.__color = color
        self.__price = price
        self.__amount = amount
        self.__delivery = delivery
        self.__setTotal()
        self.__setDiscount()
        self.__setNet()
    def __setTotal(self):
        self.__total = self.__price * self.__amount
    def __setDiscount(self):
        if self.__total >= 5000:
            self.__discount = self.__total * 0.1
        else:
            self.__discount = 0
    def __setNet(self):
        self.__net = self.__total - self.__discount
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getPattern(self):
        return self.__pattern
    def getColor(self):
        return self.__color
    def getPrice(self):
        return self.__price
    def getAmount(self):
        return self.__amount
    def getTotal(self):
        return self.__total
    def getDiscount(self):
        return self.__discount
    def getNet(self):
        return self.__net
    def getDelivery(self):
        return self.__delivery
#
class Category(models.Model):
    name = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=200,default="")
    def __str__(self):
        return  str(self.id)+" : "+ self.name +":"+ self.desc
class Product(models.Model):
    pid = models.CharField(max_length=13,primary_key=True,default="")
    name = models.CharField(max_length=50,default="")
    brand = models.CharField(max_length=50, default="")
    price = models.FloatField(default="0.00")
    net = models.IntegerField(default="0")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return  self.pid+":"+self.name+":"+self.brand+":"+ \
            str(self.price)+":"+str(self.net)+":"+self.category.name

import datetime
class Employee(models.Model):
    eid = models.CharField(max_length=5,default="",)
    name = models.CharField(max_length=35, default="", )
    surname = models.CharField(max_length=35, default="", )
    address = models.CharField(max_length=200, default="", )
    gender = models.BooleanField(default=True )
    birthdate = models.DateField(default=datetime.date.today())
    salary = models.FloatField(default=0.00)
class GoodsCategory12(models.Model):
    id = models.CharField(max_length=5, primary_key=True, default="")
    gc_name = models.CharField(max_length=35, default="")
    desc = models.CharField(max_length=200, default="")
    def __str__(self):
        return str(self.id)+ ":" + self.gc_name

class Goods12(models.Model):
    goodscategory12 = models.ForeignKey(GoodsCategory12, on_delete=models.CASCADE, default=None)
    gid = models.CharField(max_length=5, primary_key=True, default="")
    name = models.CharField(max_length=35, default="")
    brand = models.CharField(max_length=35, default="")
    model = models.CharField(max_length=35, default="")
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.CharField(max_length=200, default="")
    def __str__(self):
        return str(self.gid) + " : " + self.name + " : " + self.goodscategory12.gc_name + " : " +str(self.price)

class Customer12(models.Model):
    cid = models.CharField(max_length=5, primary_key=True, default="")
    name = models.CharField(max_length=35, default="")
    surname = models.CharField(max_length=35, default="")
    address = models.CharField(max_length=200, default="")
    telephone = models.CharField(max_length=10, default="")
    gender = models.BooleanField(default=True )
    carreer = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=10, default="")
    def __str__(self):
        return str(self.cid) + ":" + self.name + ":" + self.surname + ":" + self.carreer

class Order12(models.Model):
    oid = models.CharField(max_length=5, primary_key=True, default="")
    date = models.DateField(default=datetime.date.today())
    customer12 = models.ForeignKey(Customer12, on_delete=models.CASCADE, default=None)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.oid) + ":" + str(self.date) + ":" + self.customer12.cid + ":" + str(self.status)
class  OderDetails12(models.Model):
    id = models.CharField(max_length=5, primary_key=True, default="")
    order = models.ForeignKey(Order12, on_delete=models.CASCADE, default=None)
    goods = models.ForeignKey(Goods12, on_delete=models.CASCADE, default=None)
    price = models.FloatField(default= 0.00)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + ":" + str(self.order.oid) + ":" + str(self.goods.gid) + ":" + str(self.price)





















