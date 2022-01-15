# Generated by Django 4.0.1 on 2022-01-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_relationship', '0004_alter_language_founder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('framework', models.ManyToManyField(to='dj_relationship.Framework')),
            ],
        ),
    ]