# Generated by Django 5.0.6 on 2024-08-02 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0005_rename_name_booking_uname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='uname',
            new_name='u_name',
        ),
    ]
