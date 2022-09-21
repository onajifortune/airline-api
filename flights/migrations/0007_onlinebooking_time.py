# Generated by Django 4.1.1 on 2022-09-20 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_time_flight_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinebooking',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_time', to='flights.time'),
            preserve_default=False,
        ),
    ]
