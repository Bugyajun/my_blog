from django.shortcuts import render,redirect
from .froms import RegisterForm
# Create your views here.


def register(request):
    #如果有提交，保存数据，重定向到首页，然后可以调用django自带的用户认证进行登录，修改密码等
    #redirect_to = request.GET.get('next')
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/users/login')
    else:
        #如果没有提交，返回form渲染html，生成表单控件，让用户提交信息。
        form = RegisterForm()
        return render(request,'Users/register.html',context={'form':form})


def index(request):
    return render(request,'Users/index.html',context=None)