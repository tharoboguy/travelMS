# Generated by Django 5.0.6 on 2024-08-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0002_travels_destination_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('destination', models.CharField(max_length=225)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='travels',
        ),
    ]
