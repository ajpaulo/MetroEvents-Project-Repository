# Generated by Django 3.1.7 on 2021-03-23 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_organizer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizer',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='organizer',
            old_name='user_id',
            new_name='user',
        ),
    ]
