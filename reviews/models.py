from django.db import models
from django.urls import reverse


class Reviews(models.Model):
    """
    Model for Reviews
    """
    class Meta:
        verbose_name_plural = 'Reviews'
    review_name = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product_review = models.TextField(max_length=200)
    website_review = models.TextField(max_length=50)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('reviews')
