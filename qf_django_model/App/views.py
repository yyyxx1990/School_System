import random

from django.http import HttpResponse
from django.shortcuts import render

from App.models import Person


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(1, 100)
        # 在PyCharm中，"Tom%d" % flag是一个字符串格式化的操作，
        # 用于将变量flag的值插入到字符串中
        person.p_name = 'Tom%d' % flag
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse('批量创建成功！')


# 添加数据库第二种方式
def add_person(request):
    # person = Person.objects.create(p_name='Sunck', p_age=15, p_sex=True)
    # person.save()
    # return HttpResponse('Sunck创建成功！')
    person = Person.create('Jack')
    person.save()
    return HttpResponse('创建成功！')


def get_persons(request):
    # filter:过滤器 筛选出符合条件的内容可以级联调用
    # persons = Person.objects.filter(p_age__gt=50).filter(p_age__lt=80)
    # exclude:过滤器 剔除不符合条件的内容可以级联调用
    # persons:查询结果集
    # persons = Person.objects.exclude(p_age__lt=50).filter(p_age__lt=80)
    # print(type(persons))
    # persons_two = persons.filter(p_age__in=[50, 55, 57])
    # print(type(persons_two))
    persons = Person.objects.all().order_by('p_age')
    persons_values = persons.values()
    print(persons_values)
    # 转JSON
    for person_value in persons_values:
        print(person_value)
    context = {
        'persons': persons
    }
    return render(request, 'person_list.html', context=context)


def get_person(request):
    # 使用get要慎重，必须调用已有数据且唯一，不然得报错，
    # person = Person.objects.get(p_name=55)
    # print(person)
    # 获取第一个名字
    person = Person.objects.all().first()
    print(person.p_name)
    # 获取最后一个名字
    person_one = Person.objects.all().last()
    print(person_one.p_name)
    return HttpResponse('获取成功！')