from django.shortcuts import render,redirect
from . models import Customer,Product,Order,Add
from . forms import CustomerForm,OrderForm
# Create your views here.

def index(request):
    customer = Customer.objects.all()
    add_list = Add.objects.all()
    c_count = customer.count()

    order_p_count = Order.objects.filter(status = 'pending').count()
    order_d_count = Order.objects.filter(status='out for dilivert').count()
    order_w_count = Order.objects.filter(status='Deivered').count()

    order = Order.objects.all()
    o_count = order.count()

    c = 0
    last_five =[]
    for i in reversed(order):
        if c < 5:
            last_five.append(i)
            c+=1
        else:
            break


    if request.is_ajax and request.POST.get('order_del'):
        del_order_id = request.POST.get('order_del')
        del_order = Order.objects.get(id = del_order_id)
        del_order.delete()


    context = {
        'customer':customer,
        'add_list':add_list,
        'c_count':c_count,
        'order':order,
        'order_p_count':order_p_count,
        'order_d_count':order_d_count,
        'order_w_count': order_w_count,
        'o_count': o_count,


        'last_five':last_five
    }

    return render(request,'my_log/index.html',context)




def create(request):
    c_form = CustomerForm()
    o_form =  OrderForm()

    if request.method == 'POST':
        if 'c-button' in request.POST:
            c_form = CustomerForm(request.POST)
            if c_form.is_valid():
                name_get = c_form.cleaned_data['customer_name']
                phone_get = c_form.cleaned_data['phone']
                email_get =c_form.cleaned_data['email']
                customer = Customer.objects.create(customer_name = name_get,phone = phone_get,email =email_get)
                customer.save()
                return redirect('index')

        if 'o-button' in request.POST:
            o_form = OrderForm(request.POST)
            if o_form.is_valid():
                customer_get = o_form.cleaned_data['customer']
                product_get = o_form.cleaned_data['product']
                status_get = o_form.cleaned_data['status']
                order = Order.objects.create(customer=customer_get,product = product_get,status = status_get)
                order.save()
                return redirect('index')


    context = {
        'c_form':c_form,
        'o_form': o_form

    }


    return render(request,'my_log/create.html',context)


def update_order(request,pk):
    order = Order.objects.get(id=pk)

    o_form = OrderForm(instance=order)

    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        if o_form.is_valid():
            customer_get = o_form.cleaned_data['customer']
            product_get = o_form.cleaned_data['product']
            status_get = o_form.cleaned_data['status']
            order = Order.objects.filter(id = pk).update(id = pk, customer=customer_get, product=product_get, status=status_get)
            # order.save()
            return redirect('index')

    context = {
        'order': order,
        'o_form': o_form

    }


    return render(request,'my_log/updateorder.html',context)



def delete_order(request,pk):
    order = Order.objects.get(id = pk)


    if request.method =='POST':
        order.delete()


        return redirect('home')


    context = {
        'order': order,


    }
    return render(request,'my_log/deleteorder.html',context)

