# Generated by Django 5.0.6 on 2024-07-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlogs', '0010_management_massage'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
