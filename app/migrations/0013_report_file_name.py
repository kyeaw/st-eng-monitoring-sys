# Generated by Django 2.2.10 on 2021-11-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211101_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
