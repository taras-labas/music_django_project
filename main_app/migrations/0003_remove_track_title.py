# Generated by Django 4.2.7 on 2023-11-19 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_track_title_alter_track_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='title',
        ),
    ]
