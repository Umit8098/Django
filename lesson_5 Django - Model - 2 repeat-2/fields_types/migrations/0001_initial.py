# Generated by Django 4.0.1 on 2022-01-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('about_me', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Stud_List',
                'db_table': 'Stud_Table',
                'ordering': ['number'],
            },
        ),
    ]
