# Generated by Django 5.0.3 on 2024-05-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
