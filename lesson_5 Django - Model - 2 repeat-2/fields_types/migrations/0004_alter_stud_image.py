# Generated by Django 4.0.1 on 2022-01-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields_types', '0003_alter_stud_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
