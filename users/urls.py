from django.urls import path,include
from . import views


app_name = 'users'

urlpatterns = [
    path('login',views.login,name = 'login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),

]