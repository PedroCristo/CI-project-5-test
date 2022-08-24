from .models import *


def products_selected(request):
    """ A view to show products selected """
    products_selected = Product.objects.filter(featured=True)

    context = {
        'products_selected': products_selected,
    }

    return context


def products_promotion(request):
    """ A view to show products selected """
    products_promotion = Product.objects.filter(promotion=True)

    context = {
        'products_promotion': products_promotion,
    }

    return context    

