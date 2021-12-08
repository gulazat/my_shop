from django import forms
from django.forms import ModelForm
from .models import Customer,Order


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields =[
            'customer_name',
            'phone',
            'email'
        ]
        labels = {
            'customer_name': '姓名',
            'phone':'电话',
            'email':'邮箱'
        }
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'请输入姓名'
            }),
            'phone': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': '请输入电话'
            }),
        'email': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入邮箱'
        })

        }



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ='__all__'
        exclude = ['time_created']

        labels = {
            'customer': '顾客',
            'product': '产品',
            'status': '订单状态'
        }
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '请输入顾客'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '请输入产品'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '请输入状态'
            })

        }


