from .models import *


def products_selected(request):
    """ A view to show products selected """
    products_selected = Product.objects.filter(featured=True)

    context = {
        'products_selected': products_selected,
    }

    return context

