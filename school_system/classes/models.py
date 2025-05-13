from django.db import models


class Class(models.Model):
    object = None
    name = models.CharField(max_length=50)

    # 调用方法__str__()来显示模型来表示，返回储存在属性name里面的字符串
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    # 通过relates_name参数来覆盖默认的反向查询名称

    # 如果没有设置related_name参数，默认情况下你需要使用
    # class_obj.student_set.all()来进行反向查询。
    class_info = models.ForeignKey\
        (Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
