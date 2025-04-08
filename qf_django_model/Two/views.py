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
    # 限制查询集，可以使用下标的方法进行限制，等同于sql中limit
    # 下标不能为负数
    # 查询集的缓存：每个查询集都包含一个缓存，来最小化对数据库的访问
    # 新建查询集，缓存首次为空 django会对第一次求值的数据做一个缓存，
    # 并返回查询结构，以后的查询直接使用查询集的缓存。
    users = User.objects.all()[1:3]

    context = {
        'users': users
    }
    return render(request, 'user_list.html', context=context)