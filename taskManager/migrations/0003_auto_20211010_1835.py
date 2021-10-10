# Generated by Django 3.2.8 on 2021-10-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0002_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='projectname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='sprint',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='subtask',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]