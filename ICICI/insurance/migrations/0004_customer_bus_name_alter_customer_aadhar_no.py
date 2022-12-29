# Generated by Django 4.1 on 2022-11-24 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bus_name',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.busdetails'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='aadhar_no',
            field=models.IntegerField(default=True, null=True),
        ),
    ]
