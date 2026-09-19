from django.shortcuts import render, redirect

from shop.models import Product
from shop.forms import ProductForm


def index(request):
    data = Product.objects.all()

    return render(
        request,
        'shop/index.html',
        {'products': data}
    )


def details(request, slug):
    selected = Product.objects.get(slug=slug)

    return render(
        request,
        'shop/details.html',
        {'product': selected}
    )


def create_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():

            Product.objects.create(
                title=form.cleaned_data['name'],
                slug=form.cleaned_data['slug'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                category_id=form.cleaned_data['category_id'],
            )

            return redirect('products_list')

    else:
        form = ProductForm()

    return render(
        request,
        'shop/create-product.html',
        {'form': form}
    )