# ####
# from django.forms import *
# from .models import *
#
# class ProductForm(forms.Form):
#     BRAND_LIST = [('Brand','Brand'),('DHC', 'DHC'), ('ONCE', 'ONCE'),('Fiber', 'Fiber')]
#     TYPE_LIST = [('Capsules', 'Capsules'), ('Jelly', 'Jelly'), ('Drink', 'Drink'),]
#     DELIVERY_LIST = [('yes', 'yes'),('no', 'no')]
#
#     name = forms.CharField()
#     brand = forms.ChoiceField(widget=forms.Select, choices= BRAND_LIST, initial='Brand')
#     type = forms.ChoiceField(widget=forms.Select, choices=TYPE_LIST, initial='Capsules')
#
#     price = forms.IntegerField(min_value=0)
#     amount = forms.IntegerField(min_value=0)
#     delivery = forms.ChoiceField(widget=forms.RadioSelect,choices=DELIVERY_LIST)







# class ProductFrom(forms.Form):
#     BRAND_LIST = [('Acer','Acer',('HP','HP'),('Lennovo','Lennovo'))]
#     id = forms.CharField(max_length=13,label='รหัสสินค้า',required=True,widget=forms.TextInput(attrs={'size':'15'}))
#     name = forms.CharField(max_length=50, label='ชื่อสินค้า', required=True, widget=forms.TextInput(attrs={'size': '55'}))
#     brand = forms.CharField(max_length=30, label='ยี่ห้อ', required=True, widget=forms.Select(choices=BRAND_LIST))
#     price = forms.CharField(max_length=1.00,max_value=100000.00, label='ราคาต่อหน่วย', required=True, widget=forms.TextInput(attrs={'size': '10'}))
#     net = forms.CharField(max_length=0,max_value=1000, label='คงเหลือ', required=True, widget=forms.TextInput(attrs={'size': '10'}))
#
#
#
#
#
#
