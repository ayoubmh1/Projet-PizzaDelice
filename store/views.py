from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def products(request):
    products = Product.objects.all()
    #  obtenir les mots-clés du champ de recherche pour modifier la liste des produits
    product_name = request.GET.get("product")
    if product_name != "" and product_name is not None:
        products = products.filter(name__icontains=product_name)
    else:
        # si aucun produit n'est recherché, la valeur de l'input est vide
        product_name = ""

    # pagination de la liste des produits
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    #  recherche dans le champ de recherche 
    context = {"products": products, "search_string": product_name}
    return render(request, "store/products.html", context=context)


def pizzas(request):
    products = Product.objects.filter(product_category__name="Pizza")
    context = {"products": products}
    return render(request, "store/pizzas.html", context=context)


def drinks(request):
    products = Product.objects.filter(product_category__name="Drink")
    context = {"products": products}
    return render(request, "store/drinks.html", context=context)


def sides(request):
    products = Product.objects.filter(product_category__name="Side")
    context = {"products": products}
    return render(request, "store/sides.html", context=context)
