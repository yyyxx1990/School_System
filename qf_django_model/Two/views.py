from django.http import HttpResponse
from django.shortcuts import render

from Two.models import User


# Create your views here.
def get_user(response):
    username = 'Sunck'
    password = '911'

    users = User.objects.filter(u_name=username)
    print(users.count())
    if users.exists():
        user = users.first()

        if user.u_password ==password:
            print('获取用户信息成功！')
        else:
            print('密码错误')
    else:
        print('用户不存在！')
    return HttpResponse('获取成功')


def get_users(request):
    # 切片处理数据
    users = User.objects.all()[1:3]

    context = {
        'users': users
    }
    return render(request, 'user_list.html', context=context)