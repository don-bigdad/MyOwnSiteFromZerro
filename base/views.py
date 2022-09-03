from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import *
from .forms import UserFormQuestion, MailingForm

from django.core.paginator import Paginator

def base(request):
    if request.method == "POST":
        message = UserFormQuestion(request.POST)
        if message.is_valid():
            message.save()
            return redirect("/")
        mail = MailingForm(request.POST)
        mail.save()
        return redirect("/")

    category = Category.objects.filter(is_visible=True)


    product = Product.objects.filter(is_visible=True)

    p = Paginator(product,50)
    page = request.GET.get("page")
    prod_list = p.get_page(page)

    cart = Cart(request)

    sale_item = SaleItem.objects.filter(is_visible=True)
    form = UserFormQuestion()
    mailing = MailingForm()
    data = {
        "categories":category,
        "product":product,
        "prod_list":prod_list,
        "sale_item":sale_item,
        "form":form,
        "mailing":mailing,
        "cart":cart,
    }

    return render(request,"base.html",context=data)

