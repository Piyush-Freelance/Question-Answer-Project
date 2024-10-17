from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib. auth import authenticate, login
from .models import StudentQuestion, TeachersAnwser, Notification



def dashboard(request):
     if request.user.is_authenticated:
        user_questions = StudentQuestion.objects.filter(studentName=request.user.id)
        user_questions_count = user_questions.count()
        user_questions_answerd_count = user_questions.filter(answered=True).count()
        user_questions_pending_count = user_questions.filter(answered=False).count()
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications_count = notifications.count()

        teacher_answers = TeachersAnwser.objects.filter(student_question__in=user_questions)
     else:
         return redirect('/login')
         
     return render(request, 
                   'dashboard.html', 
                   {'user_questions': user_questions, 
                    'teacher_answers': teacher_answers, 
                    'user_questions_count':user_questions_count, 
                    'user_questions_answerd_count': user_questions_answerd_count, 
                    'user_questions_pending_count': user_questions_pending_count,
                    'notifications': notifications,
                    'notifications_count': notifications_count
                    })




def custom_404(request, exception):
    return render(request, '404.html', status=404)