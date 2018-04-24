from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.base import View
from blogs import models
from comments.forms import commentForm
#from django.views.generic import ListView,DetailView

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
    return render(request,'index.html',context={'airticle_list':airticle_list})


# class indexView(ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'context'
#     model = airticle
#
# class DetailsViews(DetailView):
#     template_name = 'blog/detail.html'
#     context_object_name = 'context'
#
#     # def get(self,request,*args,**kwargs):
#     #     response = super(DetailsViews,self).get(request,*args,**kwargs)
#     #     self.object.
#
#     # def get_object(self, queryset=None):
#     #     post = super(DetailsViews,self).get_object(self,queryset=None)
#     #
#     #     post.details =
#
#     def get_context_data(self, **kwargs):
#         context = super(DetailsViews,self).get_context_data(**kwargs)
#         form = commentForm()
#         comment_list = self.object.comment_set.all()
#         context.update({
#             'form':form,
#             'comment_list':comment_list
#         })
#         return context
#
#     def get_queryset(self):
#         #调用此试图函数时候，从url传过来的参数会放到kwargs里边，可以通过self.kwargs.get(pk)获取
#         details = get_object_or_404(models.airticle,pk=self.kwargs.get('pk'))
#         return super(DetailsViews,self).get_queryset()



