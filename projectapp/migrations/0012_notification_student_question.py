# Generated by Django 5.1 on 2024-09-07 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0011_delete_dailystudentstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='student_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectapp.studentquestion'),
        ),
    ]
