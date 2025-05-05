from django.db import models


class User(models.Model):
    objects = None
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)


class Order(models.Model):
    # 定义一个订单类，包含订单号及时间
    objects = None
    o_num = models.CharField(max_length=16, unique=True)
    # 数据库时间显示少了8小时。
    o_time = models.DateTimeField(auto_now_add=True)


class Grade(models.Model):
    objects = None
    g_name = models.CharField(max_length=16)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


# 新建消费者类
class Customer(models.Model):
    objects = None
    c_name = models.CharField(max_length=16)
    c_cost = models.IntegerField(default=10)


# 新建公司类
class Company(models.Model):
    objects = None
    c_name = models.CharField(max_length=16)
    c_gril_num = models.IntegerField(default=5)
    c_boy_num = models.IntegerField(default=3)


class AnimalManager(models.Manager):

    # get_queryset: 获取查询结果集
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=False)

    def create_animal(self, a_name='Chicken'):
        a = self.model()
        a.a_name = a_name

        return a


class Animal(models.Model):
    objects = None
    a_name = models.CharField(max_length=16)
    # 重要数据一定要逻辑删除，而不是物理删除
    is_delete = models.BooleanField(default=False)

    # 如果把隐性属性手动声明，系统就不会为你产生隐性属性
    # 会导致服务器出现AttributeError at /two/getanimals/
    # 'NoneType' object has no attribute 'all'
    # 属性错误类型
    # a_m = models.Manager()
    # 定制开始,如果注释掉下面一行代码，则输出为全部动物
    objects = AnimalManager()
