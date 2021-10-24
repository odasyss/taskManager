# Generated by Django 3.2.8 on 2021-10-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0010_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.SmallIntegerField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Testing', 'Testing'), ('Done', 'Done')], default='Not Started'),
        ),
    ]