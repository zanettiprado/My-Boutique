from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ view that renders the bag contents """

    return render(request, 'bag/bag.html')