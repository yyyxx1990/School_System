from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render

from Two.models import User, Order, Grade, Customer, Company, Animal


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


def get_orders(request):
    # orders = Order.objects.filter(o_time__year=2018)
    # django中查询条件有时区问题，按年查询可能没问题，按月或者时间查询结构查询打印不出来
    # 解决办法：1、关闭Django中自定义时区（文件DjangoModels/settings文件里面USE_TZ=False)；
    # 2、在数据库中创建对应的时区表
    orders = Order.objects.filter(o_time__month=5)

    for order in orders:
        print(order.o_num)

    return HttpResponse('获取订单成功！')


'''
跨关系查询：
    模型类名_属性名_比较运算符，实际上就是处理的数据库中的join
    grade = Grade.objects.filter(student__scontent_contains='Jack')
    描述中带有'Jack'这三个字的数据属于哪个班
'''


def get_grades(request):

    grades = Grade.objects.filter(student__s_name='Jack')

    for grade in grades:
        print(grade.g_name)

    return HttpResponse('获取成功！')


def get_customer(request):

    result = Customer.objects.aggregate(Max('c_cost'))

    result1 = Customer.objects.aggregate(Avg('c_cost'))

    print(result)

    print(result1)

    return HttpResponse('获取花费成功！')


'''
F对象：可以使用模型的A属性与B属性进行比较
grades = Grade.objects.filter(ggirlnum__gt=F('gboynum'))
F对象支持算数运算
grades = Grade.objects.filter(ggirlnum__gt=F('gboynum') + 10)

Q对象：过滤器的方法中的关键参数，常用于组合条件
语法支持|(or),&(and),~(取反）

年龄小于25
Student.objects.filter(Q(sage__lt=25))

年龄大于等于的
Student.objects.filter(~Q(sage__lt=25))
'''


def get_company(request):

    # companies = Company.objects.filter(c_boy_num__lt=F('c_gril_num'))
    # companies = Company.objects.filter(c_boy_num__lt=F('c_gril_num') - 15)
    # companies = Company.objects.filter(c_boy_num__gt=1).filter(c_gril_num__gt=5)
    companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_gril_num__gt=10))

    for company in companies:
        print(company.c_name)

    return HttpResponse('获取公司成功！')


'''
显性属性和隐性属性和定制ModelManager
'''


def get_animals(request):

    # animals = Animal.objects.all()
    # 切换到手动声明属性
    # animals = Animal.a_m.filter(is_delete=False)
    # 定制后直接查询全部
    animals = Animal.objects.all()

    for animal in animals:
        print(animal.a_name)

    # Animal.objects.create_animal()

    return HttpResponse('获取动物成功！')