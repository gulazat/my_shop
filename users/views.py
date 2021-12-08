from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import update_session_auth_hash
# from .forms import ProfileForm, SignUpForm, UserLoginForm, ChangePwdForm, SubscribeForm, FeedbackForm
from .forms import SignUpForm, UserLoginForm, ChangePwdForm
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        # next = request.POST.get('next', '/')
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
                # return redirect(next)
        else:
            print(form.errors)
    else:
        # next = request.GET.get('next', '/')
        form = UserLoginForm()
    # print(next)
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            mobile = form.cleaned_data.get('mobile')
            raw_password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username,email=email,mobile=mobile, password=raw_password1)
            auth_login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('index')


def change_password(request):
    if request.method == 'POST':
        form = ChangePwdForm(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.is_staff and not user.is_superuser:
                user.save()
                update_session_auth_hash(request, user)  # 更新session 非常重要！
                messages.success(request, '修改成功')
                return redirect('index')
            else:
                messages.warning(request, '无权修改管理员密码')
                return redirect('users:change_password')
        else:
            print(form.errors)
    else:
        form = ChangePwdForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
