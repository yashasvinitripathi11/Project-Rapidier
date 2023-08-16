from django.db import models 
from django.contrib.auth.models import User

class Student(User):
    
	
	gender_choices = (
		
		("Male", "Male"),
		("Female", "Female"),
		("Prefer not to say", "Prefer not to say")
	)
    
	bio = models.CharField(max_length = 100)

	phone_number = models.CharField(max_length = 10)
	parent_phone_number = models.CharField(max_length = 10, blank=True, null=True)
	
	address = models.TextField()

	gender = models.CharField(max_length = 17, choices = gender_choices, blank=True,null=True)

	profile_pic = models.ImageField(upload_to = "student_profile", blank=True, null=True,default = "student_profile/default.jpg")