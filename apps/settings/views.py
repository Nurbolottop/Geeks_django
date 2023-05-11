from django.shortcuts import render
from .models import Setting,About
# Create your views here.
def index(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    context = {
        'setting': setting,
        'about':about
    }
    return render(request, "index.html", context)

def contact(request):
    setting = Setting.objects.latest("id")
    context = {
        'setting': setting
    }
    return render(request, "contact.html", context)