# Generated by Django 3.2.8 on 2021-10-26 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0019_alter_task_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]
