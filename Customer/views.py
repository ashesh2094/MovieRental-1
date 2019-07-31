from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import form
from django.shortcuts import redirect
from .models import Customer

@login_required(login_url='homepage')
def customer(request, order_by="name"):
    customername= Customer.objects.all().order_by(order_by)
    return render(request,"customer.html",{
        "customername":customername
    })


def customer_delete(request,customer_id):
    c = Customer.objects.get(id=customer_id)
    c.delete()

    return redirect('/customer/all')

@login_required(login_url='homepage')
def customer_add(request):
    if request.method =='POST':
        form1 = form.addCustomer(request.POST)
        if form1.is_valid():
            # name = form1.cleaned_data["name"]
            # age = form1.cleaned_data["age"]
            # city = form1.cleaned_data["city"]
            # zipcode = form1.cleaned_data["zipcode"]
            # email = form1.cleaned_data["email"]
            # c= Customer(name=name,age=age,city=city,zipcode=zipcode,email=email)
            # c.save()
            # return redirect('/customer/all')
            a = form1.save(commit=False)
            a.save()
            return redirect('/customer/all')
    else:
        form1 = form.addCustomer()

    return render(request, 'addcustomer.html',{
        "form":form1
    } )

def customer_update(request,customer_id):
    updateData = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        form1 = form.addCustomer(request.POST , instance=updateData)
        if form1.is_valid():
            j = form1.save(commit=False)
            # print(j)
            j.save()
            return redirect('/customer/all')
    else:
        form1 = form.addCustomer(instance=updateData)

    return render(request, 'updatecustomer.html', {
        "form": form1
    })
