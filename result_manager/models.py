from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class College(models.Model):
    name        = models.CharField(max_length=100)
    address     = models.CharField(max_length=100)
    estd_date   = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name        = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    duration    = models.IntegerField()
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Student(models.Model):
    email           = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=False)
    birth_date      = models.DateField(blank=True, null=True)
    first_name      = models.CharField(max_length=50, blank=True, null=True)
    last_name       = models.CharField(max_length=50, blank=True, null=True)
    phone_number    = models.CharField(max_length=100)
    address         = models.CharField(max_length=100)
    college         = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True)
    course          = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.email}'

class Teacher(models.Model):
    email           = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=False)
    birth_date      = models.DateField(blank=True, null=True)
    first_name      = models.CharField(max_length=50, blank=True, null=True)
    last_name       = models.CharField(max_length=50, blank=True, null=True)
    phone_number    = models.CharField(max_length=100)
    address         = models.CharField(max_length=100)
    colleges        = models.ManyToManyField(College, through='Teacher_College')
    def __str__(self):
        return f'{self.email}'

class Subject(models.Model):
    name        = models.CharField(max_length=100)
    teacher     = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    course      = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    full_marks  = models.IntegerField(null = False, blank=False)
    pass_marks  = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=1000)
    credit_hours= models.IntegerField(blank=False, null=False)
    def __str__(self):
        return f'{self.name} - {self.course.course_code}'

class Exam(models.Model):
    subject     = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    semester    = models.IntegerField(blank=False, null=False)
    exam_date   = models.DateField(blank=True, null=True)
    exam_time   = models.TimeField(blank=True, null=True)
    students    = models.ManyToManyField(Student, blank=True, through="Exam_Student")
    def __str__(self):
        return f'{self.subject.name} {self.date}'

class Exam_Student(models.Model):
    student             = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    exam                = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True)
    marks_obtained      = models.IntegerField(blank=False, null=False)
    grade               = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return f'{self.student.email.username} {self.exam.subject.name}'

class Teacher_College(models.Model):
    teacher             = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    college             = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True)
    year_joined         = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.teacher.email.username} {self.college.name}'