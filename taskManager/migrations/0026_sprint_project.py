# Generated by Django 3.2.8 on 2021-11-05 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0025_auto_20211103_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskManager.project'),
            preserve_default=False,
        ),
    ]
