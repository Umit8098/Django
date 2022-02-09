# Generated by Django 4.0.2 on 2022-02-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0010_alter_student_gender_alter_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('3', 'Other'), ('1', 'Female'), ('4', 'Prefer Not Say'), ('2', 'Male')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.IntegerField(max_length=50),
        ),
    ]
