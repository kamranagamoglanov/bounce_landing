from django.shortcuts import render
from .models import Product

def home(request):
    active_posts = Product.objects.filter(is_active=True)
    return render(request, 'posts/home.html', {'posts': active_posts})