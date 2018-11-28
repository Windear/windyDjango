# Generated by Django 2.0.5 on 2018-08-29 08:49

from django.db import migrations, models
import resources.models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='file_type',
            field=models.CharField(default='sketch', max_length=100, verbose_name='文件类型'),
        ),
        migrations.AlterField(
            model_name='resources',
            name='download_address',
            field=models.FileField(upload_to=resources.models.upload_resource, verbose_name='下载链接'),
        ),
    ]
