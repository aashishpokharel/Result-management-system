from rest_framework import serializers
from result_manager.models import (
    Exam, Exam_Student, 
    Subject,
    Student, Course, College,
    Teacher, Teacher_College
)


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class ExamStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Student
        fields = '__all__'

class TeacherCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_College
        fields = '__all__'
