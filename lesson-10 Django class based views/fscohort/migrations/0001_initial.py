# Generated by Django 4.0.2 on 2022-02-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('2', 'Male'), ('4', 'Prefer Not Say'), ('1', 'Female'), ('3', 'Other')], max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('image', models.ImageField(default='avatar.png', upload_to='student/')),
            ],
        ),
    ]
