# Generated by Django 4.2.14 on 2024-10-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlogs', '0012_local_factory'),
    ]

    operations = [
        migrations.AddField(
            model_name='local_factory',
            name='type',
            field=models.CharField(blank=True, choices=[('footwear', 'Footwear'), ('leather', 'leather'), ('tannery', 'Tannery')], max_length=20, null=True),
        ),
    ]
