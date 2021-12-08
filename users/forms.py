from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=4,max_length=30,
                               error_messages={
                                   'min_length': '用户名不少于4个字符',
                                   'max_length': '用户名不能多于30个字符',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))

    email = forms.EmailField(min_length=12,max_length=30,
                             error_messages={'required': '邮件必须填写'},
                             widget=forms.TextInput(attrs={'placeholder': '请输入邮箱'}))

    mobile = forms.CharField(min_length=11,
                             error_messages={'required': '手机号必须填写'},
                             widget=forms.TextInput(attrs={'placeholder': '请输入手机好'}))


    password1 = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': '密码不少于8个字符',
                                    'max_length': '密码不能多于30个字符',
                                    'required': '密码不能为空',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))
    password2 = forms.CharField(min_length=8,max_length=30,
                                error_messages={
                                    'min_length': '密码不少于8个字符',
                                    'max_length': '密码不能多于30个字符',
                                    'required': '密码不能为空',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': '请确认密码'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

    error_messages = {'password_mismatch': '两次密码不一致', }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4,max_length=30,
                               error_messages={
                                   'min_length': '用户名不少于4个字符',
                                   'max_length': '用户名不能多于30个字符',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    password = forms.CharField(min_length=8,max_length=30,
                               error_messages={
                                   'min_length': '密码不少于8个字符',
                                   'max_length': '密码不能多于30个字符',
                                   'required': '密码不能为空',
                               },
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    error_messages = {'invalid_login': '用户名或密码错误', }

class ChangePwdForm(PasswordChangeForm):
    old_password = forms.CharField(error_messages={'required': '不能为空',},
        widget=forms.PasswordInput(attrs={'placeholder': '请输入旧密码'})
    )
    new_password1 = forms.CharField(error_messages={'required': '不能为空',},
        widget=forms.PasswordInput(attrs={'placeholder': '请输入新密码'})
    )
    new_password2 = forms.CharField(error_messages={'required': '不能为空',},
        widget=forms.PasswordInput(attrs={'placeholder': '请输入确认密码'})
    )