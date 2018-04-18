from django.shortcuts import render,redirect,get_object_or_404
from comments import models
# Create your views here.
from blogs.models import airticle

from comments.forms import commentForm

def post_comment(request,airticle_pk):
    #找到用户评论的文章
    post = get_object_or_404(airticle,pk=airticle_pk)

    if request.method == 'POST':
        forms = commentForm(request.POST)

        if forms.is_valid():

            comments = forms.save(commit=False)

            comments.airticle_id = post

            comments.save()

            return redirect(post)
        else:

            comments_list = post.comment_set.all()
            context = {
                'post':post,
                'form':forms,
                'comments_list':comments_list
             }
            return render(request,'blog/detail.html',context=context)

