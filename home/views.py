from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def about(request):
    """
    Render the about page for the restaurant.
    """
    return render(request,"about.html")   