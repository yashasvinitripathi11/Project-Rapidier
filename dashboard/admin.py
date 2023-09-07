from django.contrib import admin
from .models import Subject, Practice_Paper, Feedback, Session, Notes, Anonymous_Message, WhatsNew, Assignment, Submission
# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "description")


@admin.register(Practice_Paper)
class Practice_PaperAdmin(admin.ModelAdmin):
    list_display = ("subject", "title", "date_of_upload")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("student", "date_time")


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("title", "session_time", "is_completed", "created_at")

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("subject", "meeting", "title", "description")
    
@admin.register(Anonymous_Message)
class Anonymous_MessageAdmin(admin.ModelAdmin):
    list_display = ("student", "message", "sent_at")
    
@admin.register(WhatsNew)
class WhatsNewAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher", "created_at")
    
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("teacher", "title", "due_date", "created_at")
    
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("assignment", "student", "submitted_at")
