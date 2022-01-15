# Generated by Django 4.0.1 on 2022-01-15 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0004_alter_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
