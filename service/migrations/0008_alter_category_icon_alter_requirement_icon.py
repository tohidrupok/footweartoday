# Generated by Django 5.0.6 on 2024-06-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_rename_short_contant_requirement_short_contant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, default='photos/default.png', null=True, upload_to='category_icons/'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='icon',
            field=models.ImageField(blank=True, default='photos/default.png', null=True, upload_to='icon/'),
        ),
    ]
