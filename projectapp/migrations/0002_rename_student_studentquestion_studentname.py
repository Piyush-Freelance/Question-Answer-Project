# Generated by Django 5.1 on 2024-09-01 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentquestion',
            old_name='student',
            new_name='studentName',
        ),
    ]
