# Generated by Django 4.0.8 on 2022-11-10 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_servicestep_servicepage_step_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceindexpage',
            name='home_msg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceindexpage',
            name='home_msg_sub',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
