from django.db import models
from accounts.models import Teacher, Student, Subject


# ======================================== Practice Paper ========================================

class Practice_Paper(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True, null=True)
    file = models.FileField(upload_to="practice_papers")
    date_of_upload = models.DateTimeField(auto_now_add=True)
    
# ======================================== Feedback ========================================

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

# ======================================= Meeting ========================================


class Session(models.Model):

    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    session_time = models.DateTimeField()
    link = models.URLField()
    recorded_session_link = models.URLField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# ======================================= Notes ========================================


class Notes(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Session, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='notes')

# ======================================= Anonymous Message ========================================


class Anonymous_Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    is_replied = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

# ======================================= What's New ========================================

class WhatsNew(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
