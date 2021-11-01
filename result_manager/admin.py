from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
# admin.site.register(Class)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Exam_Student)
admin.site.register(Teacher_College)
