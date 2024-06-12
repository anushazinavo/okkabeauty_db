from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact_Stores 

def contact_stores(request):
    contacts = Contact_Stores.objects.all()
    return render(request, 'contact_us.html', {'contacts': contacts})


def okka_magazines(request):
    magazines = Contact_Stores.objects.all()
    return render(request, 'magazines.html', {'magazines': magazines})


