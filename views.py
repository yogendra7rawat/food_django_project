from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here
from .models import Input_Url
from .api_test import ingredient
from .form import get_url

def hello(request):
    #url = Input_Url()
    val = ingredient()
    context  = {"data":val}

    return render(request,'h.html',context)


def search(request):
    context = {}
    img_url = get_url()
    context['form'] =  img_url
    if request.method == 'POST':
        my_image = Input_Url(request.POST)
        temp = request.POST['image_url']
        obj = Input_Url.objects.all().values()
        for D in obj:
            for k,v in D.items():
                print(k,v)    
        # f(temp)
        return redirect("result")

    return render(request,"form.html",context)



def image_ingredient_url(url):
    return url