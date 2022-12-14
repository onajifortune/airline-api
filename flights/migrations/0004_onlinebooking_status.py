# Generated by Django 4.1.1 on 2022-09-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_onlinebooking_rename_stationpassenger_stationbooking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinebooking',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('cancelled', 'Cancelled'), ('completed', 'Completed'), ('incomplete', 'Incomplete')], default='approved', max_length=50),
        ),
    ]
