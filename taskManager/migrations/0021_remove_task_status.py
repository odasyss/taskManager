# Generated by Django 3.2.8 on 2021-11-02 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0020_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
