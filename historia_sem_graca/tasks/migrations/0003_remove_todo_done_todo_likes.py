# Generated by Django 4.0.5 on 2023-02-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
        migrations.AddField(
            model_name='todo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
