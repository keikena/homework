#from django.http import HttpResponse_4
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count

User = get_user_model()

def index(request):
    title = request.GET.get('query')

    if title:
        ads = Advertisement.objects.filter(title__icontains=title) 
        #__it - меньше чего-либо, __gt(e) - больше (или равно) ч-л
    else:
        ads = Advertisement.objects.all()
    context = {'advertisements': ads, 'title': title}
    return render(request, 'app_advertisements/index.html', context)

        
def top_sellers(request):
    users = User.objects.annotate(adv_count = Count('advertisement')).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context)


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisementForm()

    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)


def advertisement_detail(request, pk):
    ads = Advertisement.objects.get(id=pk)
    context = {'advertisement': ads}
    return render(request, 'app_advertisements/advertisement.html', context)


    