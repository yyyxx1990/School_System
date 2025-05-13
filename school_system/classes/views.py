from Doc.pycurl.examples.quickstart import get
from django.shortcuts import render, get_object_or_404

from classes.models import Class


def class_list(request):
    # 获取所有班级
    classes = Class.objects.all()

    context = {
        'classes': classes
    }

    return render(request, 'class_list.html', context=context)


def student_list(request, class_id):
    # 获取指定班级及其学生
    '''
        当需要查询某个班级的所有学生时，可以使用：
        class_obj = models.Class.objects.first()
        students = class_obj.students.all()
    '''
    class_obj = get_object_or_404(Class, id=class_id)
    context = {
        'class_obj': class_obj
    }

    return render(request, 'student_list.html', context=context)
