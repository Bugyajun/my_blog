from django.shortcuts import render,redirect,get_object_or_404
from comments import models
# Create your views here.
from blogs.models import airticle

from comments.forms import commentForm

def post_comment(request,airticle_pk):
    #找到用户评论的文章
    post = get_object_or_404(airticle,pk=airticle_pk)

    if request.method == 'POST':
        #将post的数据传给commentForm对象，用来进行表单提交到db
        forms = commentForm(request.POST)

        if forms.is_valid():

            comments = forms.save(commit=False)

            #将post赋值给comments的外键  否则提交数据的时候，不会提交airticle_id（外键）,会导致无法提交
            comments.airticle = post

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

    return redirect(post)

