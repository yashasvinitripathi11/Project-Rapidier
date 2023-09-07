from django.db import models
from accounts.models import Teacher, Student, Subject

from django.utils import timezone

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
    recorded_session_link = models.URLField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_meeting_status(self):
        now = timezone.now()
        if self.session_time > now:
            return {
                "color": "info",
                "status": "Upcoming"
            }

        elif self.is_completed:
            return {
                "color": "faded-dark",
                "status": "Finished"
            }

        elif self.session_time < now:
            return {
                "color": "danger",
                "status": "Ongoing"
            }

        else:
            return {
                "color": "danger",
                "status": "Error"
            }


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
    
    def is_of_today(self):
        return self.created_at.date() == timezone.now().date()
    
    # return how much time ago the object was created
    
    def time_ago(self):
        now = timezone.now()
        diff = now - self.created_at
        
        if diff.days > 0:
            if diff.days == 1:
                return f"{diff.days} day ago"
            else:
                return f"{diff.days} days ago"
        
        elif diff.seconds > 0:
            if diff.seconds < 60:
                return f"{diff.seconds} seconds ago"
            elif diff.seconds < 3600:
                return f"{diff.seconds // 60} minutes ago"
            else:
                return f"{diff.seconds // 3600} hours ago"
        
        else:
            return "Just now"
    
    def __str__(self):
        return self.title
    
    


# ======================================= Assignments =======================================

class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    assignment_link = models.URLField(blank=True, null=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_completed(self):
        return timezone.now() > self.due_date

    def has_submissions(self):
        return self.submissions.exists()

# ======================================= Submissions =======================================

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = models.TextField(blank=True, null=True)
    file_submission = models.FileField(upload_to='submissions/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.assignment.title}"

    class Meta:
        unique_together = ('assignment', 'student')