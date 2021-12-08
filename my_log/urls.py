from django.urls import path,include
from . import views


app_name = 'my_log'

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('create/', views.create, name='create'),
    path('updateorder/<str:pk>/', views.update_order, name='updateorder'),
    path('deleteorder/<str:pk>/', views.delete_order, name='deleteorder')

]