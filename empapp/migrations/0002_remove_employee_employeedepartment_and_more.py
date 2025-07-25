# Generated by Django 5.0.4 on 2025-05-08 09:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employeeDepartment',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employeeEmail',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employeeName',
        ),
        migrations.AddField(
            model_name='employee',
            name='addressDetails',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='companyName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='fromDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='hno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='phoneNo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='photos/default.jpeg', upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='employee',
            name='qualificationName',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='employee',
            name='qualifications',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='toDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='workExperience',
            field=models.JSONField(default=dict),
        ),
    ]
