# Generated by Django 3.1.7 on 2021-03-23 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('organizer', '0006_delete_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('par_id', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'participant',
            },
        ),
    ]
