from django.core.exceptions import BadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from services.products_module.models import Product, Currency
from services.products_module.forms import UpdateProductForm
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
@register.filter
def get_range(value):
    return range(1, value + 1)
def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"products": page_obj, "pages_count": paginator.num_pages, 'page_number': page_number}
    return render(request, "index.html", context)

@login_required
def get_my_products(request):
    products = Product.objects.filter(owner=request.user)
    paginator = Paginator(products, 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"products": page_obj, "pages_count": paginator.num_pages, 'page_number': page_number}
    return render(request, "my_products.html", context)


def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", context={"product": product, "is_my_product": True})

@login_required
def create_product(request):
    if request.method == "POST":
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            try:
                currency = get_object_or_404(Currency, pk=int(form.data["currency"]))

            except ValueError:
                return BadRequest("Invalid currency field")

            product = Product.objects.create(title=form.data["title"],
                                             description=form.data["description"],
                                             price=form.data["price"],
                                             in_stock=True if form.data.get("in_stock", False)
                                             else False,
                                             owner=request.user,
                                             currency=currency)

            return redirect("product", pk=product.pk)
    else:
        form = UpdateProductForm()
    currency_list = Currency.objects.all()
    return render(request, "create_update_product.html", context={"form": form, "currency_list": currency_list })


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            try:
                currency = get_object_or_404(Currency, pk=int(form.data["currency"]))

            except ValueError:
                return BadRequest("Invalid currency field")

            product.title = form.data["title"]
            product.description = form.data["description"]
            try:
                product.price = float(form.data["price"])
            except ValueError:
                return BadRequest("Invalid price field")
            product.in_stock = True if form.data.get("in_stock", False) else False
            product.currency = currency

            product.save()

            return redirect("product", pk=product.pk)

    form = UpdateProductForm(data={'title': product.title,
                                   'description': product.description,
                                   'price': product.price,
                                   'in_stock': product.in_stock,
                                   'currency': product.currency})

    currency_list = Currency.objects.all()
    return render(request, "create_update_product.html", context={"form": form, "product": product, "currency_list": currency_list, "is_my_product": True})


def delete_product(request, pk):
    get_object_or_404(Product, pk=pk).delete()
    return redirect("get_my_products")
