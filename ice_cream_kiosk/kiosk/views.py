from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from kiosk.models import Kiosk, IceCream


def kiosk_list(request):
    kiosks = Kiosk.objects.all()
    return render(request, 'kiosk/kiosk_list.html', {'kiosks': kiosks})

def ice_cream_list(request):
    ice_creams = IceCream.objects.all()
    return render(request, 'kiosk/ice_cream_list.html', {'ice_creams': ice_creams})

def ice_cream_search(request):
    query = request.GET.get('q', '')
    ice_creams = IceCream.objects.filter(flavor__icontains=query)
    return render(request, 'kiosk/ice_cream_search.html', {'ice_creams': ice_creams, 'query': query})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'kiosk/signup.html', {'form': form})

@login_required
def user_profile(request):
    return render(request, 'kiosk/user_profile.html')

