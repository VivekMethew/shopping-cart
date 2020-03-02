from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductDetail, Contact, Orders, orderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    # products = ProductDetail.objects.all()
    # print(products)
    # n = len(products)
    # nSlide = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = ProductDetail.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = ProductDetail.objects.filter(category=cat)
        n = len(prod)
        nSlide = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlide), nSlide])
    # params = {'no_of_slides':nSlide, 'range':range(1,nSlide),'product':products}
    # allProds = [[products, range(1,nSlide), nSlide],
    #             [products, range(1,nSlide), nSlide]]
    params = {'allProds':allProds}           
    return render(request, 'shop/index.html',params)

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def productview(request, myid):
    # Fetch the product with id
    product = ProductDetail.objects.filter(id=myid)
    # print(product)
    return render(request, 'shop/product.html', {'product':product[0]})

def search(request):
    return render(request, 'shop/search.html')

def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = orderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates, order[0].item_json], default=str)
                return HttpResponse(response)                   
            else:
                return HttpResponse('{}') 
        except Exception as e:
            return HttpResponse('{}')       
    return render(request, 'shop/tracker.html')   

def checkout(request):
    if request.method=="POST":
        print(request)
        item_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipCode = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(item_json=item_json,name=name,amount=amount, email=email,address=address, city=city, state=state, zip_code=zipCode, phone=phone)
        order.save()
        update = orderUpdate(order_id=order.order_id, update_desc="The Order has been Placed!")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after paytm by user.
    return render(request, 'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    # Paytm will send you post request here.
    pass    


