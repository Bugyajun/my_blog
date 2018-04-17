from django.shortcuts import render,redirect,get_object_or_404
from blogs import models

# Create your views here.
def index(request):
    context = models.airticle.objects.all().order_by('-update_time')

    return render(request,'blog/index.html',context={'context':context})

def detail(request,pk):
    post = get_object_or_404(models.airticle,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})


