# Generated by Django 5.0.4 on 2025-05-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0003_alter_employee_city_alter_employee_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='photos/default.jpeg', max_length=500, upload_to='photos/'),
        ),
    ]
