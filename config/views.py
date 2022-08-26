
from django.http import HttpResponse
from django.shortcuts import render
# from wallet.models import Cuzdan

def home(request):
    
    context = {}

    if request.user.is_authenticated:
        context['cuzdanlar'] = request.user.cuzdanlar.all()

    # cuzdanlar = Cuzdan.objects.filter(user = request.user)
    # print(dir(request))    

    return render(request, "index.html", context)

def isim_yaz(request,isim):
    return render(request, "isim.html", {'isim': isim})

def python(request):
    return HttpResponse('Bunu göremezsin')

def ad_soyad_yaz(request, ad, soyad):
    return render(request, "adSoyad.html", {'ad': ad, 'soyad':soyad})