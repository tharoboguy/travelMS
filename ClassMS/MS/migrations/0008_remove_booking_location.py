# Generated by Django 5.0.6 on 2024-08-05 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0007_rename_checkin_booking_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='location',
        ),
    ]
