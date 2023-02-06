from django import forms
from .models import *

class ProductForm11(forms.Form):
    PATTERN_LIST = (('Street', 'Street'), ('Hawaii', 'Hawaii'), ('Lovely', 'Lovely'),
                                        ('Pastal', 'Pastall'),('ColorBlock','ColorBlock'),)
    COLOR_LIST = (('white', 'white'), ('black', 'black'), ('orange', 'orange'), ('blue', 'blue'))
    DELIVERY_LIST = (('Delivery', 'Delivery'), ('No', 'No'))
    id = forms.CharField()
    name = forms.CharField()
    pattern = forms.ChoiceField(widget=forms.Select, choices=PATTERN_LIST, initial='white')
    color = forms.ChoiceField(widget=forms.Select, choices= COLOR_LIST, initial='สีดำ')
    price = forms.IntegerField(min_value=0)
    amount = forms.IntegerField(min_value=0)
    delivery = forms.ChoiceField(widget=forms.RadioSelect,choices=DELIVERY_LIST)

##############
class ProductMForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pid', 'name','brand', 'price', 'net','category')
        widgets ={
            'pid':forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control','required':'required','max_length':35}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        lables ={
            'pid':'ID',
            'name':'name',
            'brand': 'brand',
            'net': 'net',
            'category': 'category',
            }
        def updateMForm(self):
            self.fields['pid'].widget.attrs['readonly']=True
            self.fields['pid'].labels='รหัสสินค้า [ไม่อนุญาตให้แก้ไขได้]'
class ProductUpdateMForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pid', 'name','brand', 'price', 'net','category')
        widgets ={
            'pid':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control','required':'required','max_length':35}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        lables ={
            'pid':'ID',
            'name':'name',
            'brand': 'brand',
            'net': 'net',
            'category': 'category',
            }

class GoodsForm12 (forms.ModelForm):
    class Meta:
        model = Goods12
        fields =('goodscategory12', 'gid', 'name', 'brand', 'price','model', 'net', 'property')
        widgets = {
            'goodscategory12': forms.Select(attrs={'class':'form-control'}),
            'gid': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control','min':1}),
            'net': forms.NumberInput(attrs={'class':'form-control','min':0}),
            'property': forms.Textarea(attrs={'class':'form-control','rows': 3, 'cols': 60}),
        }
        labels = {
            'goodscategory12':'Goodscategory',
            'gid':'Goodsid',
            'name':'Goodsname',
            'brand':'Brand',
            'model':'Models',
            'price':'Price',
            'net':'Net',
            'property':'Property',
        }
