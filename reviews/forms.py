from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """
    Form for Reviews
    """
    class Meta:
        model = Reviews
        fields = ('review_name', 'image', 'product_review', 'website_review', 'rating')