# Generated by Django 4.1 on 2022-10-31 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapplication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeldis',
            name='company',
        ),
        migrations.RemoveField(
            model_name='modeldis',
            name='company_details',
        ),
    ]
