# Generated by Django 5.1.1 on 2024-10-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_showtimes_st'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtimes',
            name='seatprice',
            field=models.IntegerField(default=200),
        ),
    ]
