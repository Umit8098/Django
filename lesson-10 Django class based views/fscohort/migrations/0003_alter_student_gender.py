# Generated by Django 4.0.2 on 2022-02-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0002_alter_student_options_alter_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('2', 'Male'), ('1', 'Female'), ('4', 'Prefer Not Say'), ('3', 'Other')], max_length=50),
        ),
    ]
