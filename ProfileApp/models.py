# from django.db import models
# class Product:
#     def __init__(self,name,type,brand,price,amount,delivery):
#         self.name = name
#         self.type = type
#         self.brand = brand
#         self.price = price
#         self.delivery = delivery
#         self.amount = amount
#         self.__setTotal()
#         self.__setPriceDeli()
#         self.__setDiscount()
#         self.__setNet()
#     def __setPriceDeli(self):
#         if self.delivery == "yes":
#             self.priceDeli = 100
#         else:
#             self.priceDeli = 0
#     def __setTotal(self):
#         self.total = (self.price *self.amount) + self.priceDeli
#     def __setDiscount(self):
#         if self.total >= 5000 :
#             self.discount = 500
#         else:
#             self.discount = 0
#     def __setNet(self):
#         self.net = self.total - self.discount
#
#
#     def getName(self):
#         return self.name
#     def getType(self):
#         return self.type
#     def getBrand(self):
#         return self.brand
#     def getPrice(self):
#         return self.price
#     def getAmount(self):
#         return self.amount
#     def getDelivery(self):
#         return self.delivery



    #

    # def __str__(self):
    #     return "ID:{},Name:{},Brabd:{},Price{},Net{}".format(self.id,self.name,self.brand,self.price,self.net)

