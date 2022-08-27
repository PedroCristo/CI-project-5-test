from .models import *


def customers_reviews(request):
    """ A view to show customers reviews """
    reviews = Reviews.objects.all().filter(
        approved=True).order_by("-timestamp")

    context = {
        'reviews': reviews,
    }

    return context