# Generated by Django 3.2.8 on 2021-10-13 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0004_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtask',
        ),
    ]
