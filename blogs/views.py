from django.shortcuts import render,redirect,get_object_or_404
from blogs import models
from comments.forms import commentForm

# Create your views here.
def index(request):
    context = models.airticle.objects.all().order_by('-update_time')

    return render(request,'blog/index.html',context={'context':context})

def detail(request,pk):
    post = get_object_or_404(models.airticle,pk=pk)

    form = commentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list
    }


    return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
    airticle_list = models.airticle.objects.filter(create_time__year=year,
                                                         create_time__month=month
                                                         ).order_by('-create_time')
    return render(request,'archives.html',context={'airticle_list':airticle_list})




