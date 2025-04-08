from django.db import models


class Person(models.Model):
    # 用户名不允许重复，加约束unique=True
    objects = None
    p_name = models.CharField(max_length=16, unique=True)
    # default:默认的;db_column修改数据库列的名由p_age改为age
    p_age = models.IntegerField(default=18, db_column='age')
    # 默认False代表男；True代表女。
    p_sex = models.BooleanField(default=False, db_column='sex')
    # 添加新属性数据就得修改python manage.py makemigrations，
    # 再迁移python manage.py migrate
    p_hobby = models.CharField(max_length=32, null=True, blank=True)

    # 装饰器，用于定义类方法
    @classmethod
    def create(cls, p_name, p_age=100, p_sex=True, p_hobby='gaming'):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    # 设置元信息
    class Meta:
        db_table = 'People'
