# Generated by Django 4.1 on 2022-11-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_busdetails_destination_route_delete_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('sex', models.CharField(choices=[('male', 'male'), ('Female', 'Female'), ('other', 'other')], max_length=200)),
                ('aadhar_no', models.IntegerField(null=True)),
            ],
        ),
    ]
