# my_app/utils.py
from .models import DailyStudentStats
from datetime import date

def update_daily_stats(student, asked, answered, pending):
    today = date.today()
    stats, created = DailyStudentStats.objects.update_or_create(
        student=student,
        date=today,
        defaults={
            'asked_count': asked,
            'answered_count': answered,
            'pending_count': pending
        }
    )
    return stats
