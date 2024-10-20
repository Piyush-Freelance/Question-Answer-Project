# Generated by Django 5.1 on 2024-09-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0008_dailystudentstats'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailystudentstats',
            options={},
        ),
        migrations.AlterField(
            model_name='dailystudentstats',
            name='answered_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailystudentstats',
            name='asked_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailystudentstats',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dailystudentstats',
            name='pending_count',
            field=models.IntegerField(),
        ),
    ]
