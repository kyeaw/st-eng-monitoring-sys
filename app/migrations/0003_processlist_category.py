# Generated by Django 2.2.10 on 2021-10-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_logdata_processlist_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='processlist',
            name='category',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
