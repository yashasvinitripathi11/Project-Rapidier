from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.utils import timezone
from django.contrib import messages

from accounts.models import Student
from dashboard.models import Session, Assignment, Submission, Notes, Anonymous_Message, WhatsNew
from .models import Feedback

@login_required(login_url='signin')
def dashboard(request):
    
    student = Student.objects.get(id=request.user.id)
    student_subjects = student.subjects.all()
    
    current_time = timezone.localtime(timezone.now())
    today_start = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = current_time.replace(hour=23, minute=59, second=59, microsecond=999999)
    sessions_today = Session.objects.filter(subject__in=student_subjects, session_time__range=(today_start, today_end), is_completed=False)
    
    completed_sessions = Session.objects.filter(subject__in=student_subjects, is_completed=True)
    
    incomplete_assignments = Assignment.objects.filter(subject__in=student_subjects, due_date__gte=timezone.now())
    
    total_submissions = Submission.objects.filter(student=student).count()
    
    parameters = {
        "student": student,
        "sessions_today": sessions_today,
        "completed_sessions": completed_sessions,
        "incomplete_assignments": incomplete_assignments,
        "total_submissions": total_submissions,

    }
    
    return render(request, "dashboard/dashboard.html", parameters)

# ======================================== Meeting ========================================

@login_required(login_url='signin')
def meeting(request):
    
    student = Student.objects.get(id=request.user.id)
    student_subjects = student.subjects.all()
    
    completed_sessions = Session.objects.filter(subject__in=student_subjects, is_completed=True)

    parameters = {
        "student": student,
        "completed_sessions": completed_sessions,
        'has_notification': WhatsNew.has_notification(),

    }
    
    return render(request, "dashboard/meeting.html", parameters)

# ======================================== Assignments ====================================

@login_required(login_url='signin')
def assignments(request):
    
    student = Student.objects.get(id=request.user.id)
    student_subjects = student.subjects.all()
    
    assignments = Assignment.objects.filter(subject__in=student_subjects)
    print(assignments)
    
    parameters = {
        "student": student,
        "assignments": assignments
    }
    
    return render(request, "dashboard/assignments.html", parameters)

# ======================================== Notes ========================================

@login_required(login_url='signin')
def notes(request):
    
    student = Student.objects.get(id=request.user.id)
    subjects = student.subjects.all()
    
    notes = Notes.objects.filter(subject__in=subjects)
    
    parameters = {
        "student": student,
        "subjects": subjects,
        "notes": notes
    }
    
    return render(request, "dashboard/notes.html", parameters)

# ======================================== Whats New ======================================

@login_required(login_url='signin')
def whatsnew(request):
    
    student = Student.objects.get(id=request.user.id)
    
    whatsnew = WhatsNew.objects.all()[::-1]
    
    
    parameters = {
        "student": student,
        "whatsnew": whatsnew,
        'has_notification': WhatsNew.has_notification(),

    }
    return render(request, "dashboard/whatsnew.html", parameters)


@login_required(login_url='signin')
def quiz(request):
    return render(request, "dashboard/quiz.html")


@login_required(login_url='signin')
def exampaper(request):
    return render(request, "dashboard/exampaper.html")



@login_required(login_url='signin')
def test(request):
    return render(request, "dashboard/test.html")


@login_required(login_url='signin')
def profile(request):
    student = Student.objects.get(id=request.user.id)
    total_submissions = Submission.objects.filter(student=student).count()

    parameters = {
        "student": student,
        "total_submissions": total_submissions
    }
    
    return render(request, "dashboard/profile.html", parameters)

# ============================================== Edit Profile ==============================================


@login_required(login_url='signin')
def edit_profile(request):

    student = Student.objects.get(id=request.user.id)

    if request.method == "POST":

        student.first_name = request.POST.get("first_name")

        student.last_name = request.POST.get("last_name")

        student.phone_number = request.POST.get("phone_number")

        student.address = request.POST.get("address")

        student.parent_phone_number = request.POST.get("parent_phone_number")

        student.gender = request.POST.get("gender")

        student.bio = request.POST.get("bio")

        student.save()
        
        messages.success(request, 'Profile Updated Successfully!')
        
        return redirect("profile")

    return render(request, "dashboard/edit_profile.html", {"student": student})

# ======================================== Update Profile Picture ==========================================


@login_required(login_url='signin')
def update_profile_pic(request):
    student = Student.objects.get(id=request.user.id)

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')

        student.profile_pic = profile_pic

        student.save()
        
        messages.success(request, 'Profile Picture Updated Successfully!')

        return redirect('profile')

    return render(request, 'dashboard/update_profile_pic.html', {"student": student})


# ======================================== Update Banner Image ==========================================

@login_required(login_url='signin')
def update_banner_image(request):
     student = Student.objects.get(id=request.user.id)

     banner_image = request.FILES.get('banner_image')

     student.banner_image = banner_image

     student.save()
     
     messages.success(request, 'Banner Image Updated Successfully!')

     return redirect('profile')

# ============================================== Delete Account ==============================================

@login_required(login_url='signin')
def delete_account(request):
    student = Student.objects.get(id=request.user.id)

    student.delete()
    auth.logout(request)

    return redirect('home')

# ============================================== Change Password ==============================================

@login_required(login_url='signin')
def change_password(request):
    student = Student.objects.get(id=request.user.id)

    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    confirm_password = request.POST.get('confirm_password')

    if student.check_password(old_password):
        if new_password == confirm_password:
            student.set_password(new_password)
            student.save()
            auth.logout(request)
            messages.success(request, 'Password Changed Successfully! Please Login Again!')
            return redirect('signin')
        else:
            messages.error(
                request, 'New Password and Confirm Password does not match!')
            return redirect('profile')
    else:
        messages.error(request, 'Old Password is Incorrect!')
        return redirect('profile')
# ============================================== Feedback ==============================================


@login_required(login_url='signin')
def feedback(request):
    student = Student.objects.get(username=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')

        new_feedback = Feedback.objects.create(
            student=student,
            message=message
        )

        new_feedback.save()

        messages.success(request, 'Thanks for your valuable Feedback!')

        return redirect('feedback')

    parameters = {
        "student": student
    }

    return render(request, 'dashboard/feedback.html', parameters)


# ============================================== Submit Assignment ==============================================

@login_required(login_url='signin')
def submit_assignment(request, assignment_id):
    student = Student.objects.get(id=request.user.id)
    assignment = Assignment.objects.get(id=assignment_id)

    if request.method == 'POST':
        file = request.FILES.get('file')
        answer = request.POST.get('answer')

        new_submission = Submission.objects.create(
            student=student,
            assignment=assignment,
            file_submission=file,
            answer=answer
        )

        new_submission.save()

        messages.success(request, 'Assignment Submitted Successfully!')

        return redirect('dashboard')

    parameters = {
        "student": student,
        "assignment": assignment
    }

    return render(request, 'dashboard/submit_assignment.html', parameters)
