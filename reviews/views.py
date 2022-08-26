from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Reviews
from .forms import ReviewsForm
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def reviews(request):
    """ 
    Renders the reviews page
    """
    reviews_list = Reviews.objects.all().filter(
        approved=True).order_by("-timestamp")
    return render(request, 'reviews/reviews.html', {'reviews_list': reviews_list})



class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Renders the Add Review page
    """
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/add_edit_review.html'
    success_message = """Your Review was sent successfully 
                            and is awaiting approval!"""

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)    
