from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from projectapp.models import StudentQuestion, TeachersAnwser, Notification
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .forms import PasswordResetForm


def index(request):
     return render(request, 'index.html')


def loginn(request):

    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:

                return redirect('/you-are-staff')
            else:

                auth_login(request, user)
                return redirect('/dashboard')
        else:

            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')



def register(request):

    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username = username, password = password, email = email)
        return redirect('/login')
    return render(request, 'register.html')

def logout_view(request):
    is_staff = request.user.is_staff
    logout(request)
    if is_staff:
        return redirect('/teacherCanLoginHere')
    else:
        return redirect('/')





def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = None

            # Try to find the user by username or email
            if username:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    form.add_error('username', 'User with this username does not exist.')
            elif email:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    form.add_error('email', 'User with this email does not exist.')

            # If user exists, generate password reset email
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                # Send the email (replace with real email sending)
                reset_link = request.build_absolute_uri(f"/reset/{uid}/{token}/")
                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_link}',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )
                return redirect('password_reset_done')
    else:
        form = PasswordResetForm()

    return render(request, 'reset_password.html', {'form': form})

    


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        user_questions = StudentQuestion.objects.filter(studentName=request.user.id)
        user_questions_count = user_questions.count()
        user_questions_answerd_count = user_questions.filter(answered=True).count()
        user_questions_pending_count = user_questions.filter(answered=False).count()
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications_count = notifications.count()
        return render(request, 'profile.html',
                       {'user': user,
                        'user_questions_count':user_questions_count, 
                        'user_questions_answerd_count': user_questions_answerd_count, 
                        'user_questions_pending_count': user_questions_pending_count,
                        'notifications': notifications,
                        'notifications_count': notifications_count
                        })
    else:
        return redirect('/login')
    




def addQuestion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            subject = request.POST.get('subject')
            question = request.POST.get('question')
            StudentQuestion.objects.create(
                studentName=request.user,
                subject=subject,
                question=question
            )
            return redirect('/dashboard')
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications_count = notifications.count()
        return render(request, 'ask.html',{
                    'notifications': notifications,
                    'notifications_count': notifications_count
                      })
    else:
        return redirect('/login?r=login_first')


def allStudentQuestions(request):
    if request.user.is_authenticated:
        user_questions = StudentQuestion.objects.filter(studentName=request.user.id)
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications_count = notifications.count()
        return render(request, 'all-questions.html', {'allQuestions': user_questions, 'notifications': notifications,
                    'notifications_count': notifications_count})
    else:
        return redirect('/login?r=login_first')
    



def teacherLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                auth_login(request, user)
                return redirect('/teacher/questions') 
            else:
                messages.error(request, "Dont try to be smart, You kid, Log in as a student.")
                return redirect('/teacherCanLoginHere')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'teacherLogin.html')






def allStudentQuestions(request):
    if request.user.is_authenticated and request.user.is_staff:
        user_questions = StudentQuestion.objects.filter(answered=False)
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications_count = notifications.count()
        return render(request, 'teacher/questions.html', {'allQuestionsForTeacher': user_questions,'notifications': notifications,
                    'notifications_count': notifications_count})
    else:
        return redirect('/permission-denied')
    


def submitAns(request, question_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('/permission-denied')

    user_questions = get_object_or_404(StudentQuestion, pk=question_id)

    already_answered = ""  

    if request.method == "POST":
        answer = request.POST.get('answer')
        if not answer:
            return render(request, 'teacher/submit_answer.html', {
                'specficQuestionsForTeacher': user_questions,
                'error': 'Answer cannot be empty',
                'already_answered': already_answered
            })

        existing_answer = TeachersAnwser.objects.filter(student_question=user_questions).first()
        if existing_answer:
            already_answered = existing_answer.answer  
            existing_answer.answer = answer
            existing_answer.save()
        else:
            TeachersAnwser.objects.create(
                TeacherName=request.user,
                answer=answer,
                student_question=user_questions
            )

        user_questions.answered = True
        user_questions.save()

        return redirect('/teacher/allAnswered/')

    existing_answer = TeachersAnwser.objects.filter(student_question=user_questions).first()
    if existing_answer:
        already_answered = existing_answer.answer

    return render(request, 'teacher/submit_answer.html', 
                  {'specficQuestionsForTeacher': user_questions,
                   'already_answered': already_answered
                  })



def allAnswerdByTeacher(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('/permission-denied')
     
    all_teacher_answer = TeachersAnwser.objects.filter(TeacherName = request.user)
    return render(request, 'teacher/all_answered.html', {'all_teacher_answers': all_teacher_answer})




def allQuestionsAndAnswers(request):
    QuestionsAndAnswers = TeachersAnwser.objects.all()
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    notifications_count = notifications.count()
    return render(request, 'questions-anwers.html', {'QuestionsAndAnswers': QuestionsAndAnswers,'notifications': notifications,
                    'notifications_count': notifications_count})




def perticular_Ans(request, student_question_id):
    student_question = get_object_or_404(StudentQuestion, pk=student_question_id)
    particular_ans = TeachersAnwser.objects.filter(student_question=student_question).first()
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    notifications_count = notifications.count()
    return render(request, 'particular_ans.html', {
        'student_question': student_question,
        'particular_ans': particular_ans,
        'notifications': notifications,
        'notifications_count': notifications_count
    })


def permission_denied(request):
    return render(request, 'permisssion-decline.html')



def student_notifications_view(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    
    return render(request, 'notifications.html', {'notifications': notifications})




def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.read = True
    notification.save()
    return redirect('/dashboard')   



def custom_404(request, exception):
    return render(request, '404.html', status=404)