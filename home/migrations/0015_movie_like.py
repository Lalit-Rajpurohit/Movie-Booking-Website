# Generated by Django 5.1.1 on 2024-10-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_showtimes_seatprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='like',
            field=models.IntegerField(default=92),
        ),
    ]
