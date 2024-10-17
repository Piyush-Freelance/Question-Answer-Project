"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import perticular_Ans
from django.conf.urls import handler404
from .views import reset_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.loginn),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('profile/', views.profile),
    path('ask/', views.addQuestion),
    path('all/', views.allStudentQuestions),
    path('teacherCanLoginHere/', views.teacherLogin),
    path('teacher/questions/', views.allStudentQuestions),
    path('teacher/allAnswered/', views.allAnswerdByTeacher),
    path('teacher/questions/<int:question_id>', views.submitAns),
    path('sarkari/', views.allQuestionsAndAnswers),
    path('permission-denied/', views.permission_denied),
    path('sarkari/<int:student_question_id>', perticular_Ans),
    path('notifications/', views.student_notifications_view, name='student_notifications_view'),
    path('notification/read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('dashboard/', include('projectapp.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]

# Set the custom 404 handler
handler404 = 'projectapp.views.custom_404'