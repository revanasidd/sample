from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.
def home(request):
	customers=Customer.objects.all()
	orders=Order.objects.all()

	total_customer=customers.count()
	total_order=orders.count()

	devliverd=orders.filter(status='Delivered').count()
	pending=orders.filter(status='Pending').count()

	context={'orders':orders,'customers':customers,'total_customer':total_customer,
	'total_order':total_order,'devliverd':devliverd,'pending':pending}	
	return render(request,'account/dashboard.html',context )

def products(request):
	productss=Product.objects.all()
	return render(request, 'account/products.html',{'productss':productss})

def Customers(request,pk):
	customer=Customer.objects.get(id=pk)
	orders=customer.order_set.all()
	order_count=orders.count()
	context={'customer':customer,'orders':orders,'order_count':order_count}
	return render(request,'account/customer.html',context)

def Createorder(request):
	form=OrderForm()
	if request.method=='POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request, 'account/order_form.html',context)

def updateOrder(request,pk):
	form=OrderForm()
	order=Order.objects.get(id=pk)
	form=OrderForm(instance=order)
	if request.method=='POST':
		form=OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'account/order_form.html',context)

def deleteOrder(request,pk):
	order=Order.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return redirect('/')
	context={'item':order}
	return render(request,'account/delete.html',context)
