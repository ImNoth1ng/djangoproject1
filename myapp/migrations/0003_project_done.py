# Generated by Django 4.2.7 on 2023-11-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
