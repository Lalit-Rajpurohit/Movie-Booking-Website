# Generated by Django 5.1.1 on 2024-09-12 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_date_time_alter_showtimes_movie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showtimes',
            old_name='show_date',
            new_name='show_dates',
        ),
        migrations.RenameField(
            model_name='showtimes',
            old_name='show_time',
            new_name='show_times',
        ),
    ]
