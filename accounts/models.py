from django.db import models
from django.contrib.auth.models import User


# =================================================== Teacher ==========================================

class Teacher(User):
    phone_number = models.CharField(max_length=10)

    bio = models.CharField(max_length=100, blank=True, null=True)

    profile_pic = models.ImageField(
        upload_to="teacher_profile", blank=True, null=True)

    gender = models.CharField(max_length=19, choices=(
        ("Male", "Male"),	("Female", "Female"), ("Prefer not say", "Prefer not say")))

    class Meta:
        verbose_name_plural = "Teachers"
        verbose_name = "Teacher"
         
    def __str__(self):
        return self.username
    
# =================================================== Subject ==========================================
    
class Subject(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="subject_image", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
# =================================================== Student ==========================================

class Student(User):
    gender_choices = (

        ("Male", "Male"),
        ("Female", "Female"),
        ("Prefer not to say", "Prefer not to say")
    )

    bio = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=10)
    parent_phone_number = models.CharField(
        max_length=10, blank=True, null=True)

    address = models.TextField()

    gender = models.CharField(
        max_length=17, choices=gender_choices, blank=True, null=True)
    
    subjects = models.ManyToManyField(Subject, blank=True, null=True)

    profile_pic = models.ImageField(
        upload_to="student_profile", blank=True, null=True, default="student_profile/default.jpg")

    class Meta:
        verbose_name_plural = "Students"
        verbose_name = "Student"
