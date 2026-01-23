from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    # return HttpResponse('this is home-page')
    context={
        "variable":"twenty",
        "show_footer": True 
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method== 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        description= request.POST.get('description')
        contact= Contact(first_name=first_name, last_name=last_name, phone=phone, email=email, description=description, date= datetime.today())
        contact.save()
        messages.success(
            request,
            "! .Well done Your message has been sent successfully"
        )
    return render(request, 'contact.html')

def lists(request):
    return render(request, 'lists.html')

def arrivals(request):
    return render(request, 'arrivals.html')

def about(request):
    return render(request, 'about.html')

# def about(request):
#     return HttpResponse('this is about page')

def cart(request):
    cart = request.session.get("cart", {})
    return render(request, "cart.html", {"cart": cart})

def add_to_cart(request):
    if request.method == "POST":
        cart = request.session.get("cart", {})

        product_id = request.POST["id"]
        name = request.POST["name"]
        price = request.POST["price"]

        cart[product_id] = {
            "name": name,
            "price": price,
        }

        request.session["cart"] = cart

    return redirect("cart")


