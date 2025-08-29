from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def about(request):
    """
    Render the about page for the restaurant.
    """
    return render(request,"about.html")

def index(request):
    """
    Render the homepage with restaurant name from database
    """   
    restaurant = Restaurant.objects.first()  # considering the single record
    context = {
        "restaurant_name" : restaurant.name if restaurant else "Our Restaurant"

    }
    return render(
        request=request,
        template_name = "index.html",
        content = content 
    )

