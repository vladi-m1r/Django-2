from django.shortcuts import render

from travelloApp.models import Destination

# Create your views here.
def index(request):
    destinos = Destination.objects.all()
    return render(request, "index.html", {"destinos": destinos})