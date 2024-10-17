from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class StudentQuestion(models.Model):
    studentName = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    question = RichTextField()
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    student_question = models.ForeignKey(StudentQuestion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Notification for {self.recipient.username}'






class TeachersAnwser(models.Model):
    TeacherName = models.ForeignKey(User, on_delete=models.CASCADE)
    student_question = models.OneToOneField(StudentQuestion, on_delete=models.CASCADE)
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.student_question.answered = True
        self.student_question.save()

        
        Notification.objects.create(
            recipient=self.student_question.studentName,
            message=f'Your question on "{self.student_question.subject}" has been answered by {self.TeacherName.username}.',
            student_question=self.student_question  
        )

    def __str__(self):
        return f'Answer by {self.TeacherName.username} to {self.student_question.subject}'