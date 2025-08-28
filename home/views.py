from django.shortcuts import render

# Create your views here.
def about(request):
    """
    Render the about page for the restaurant.
    """
    return render(request,"about.html")   