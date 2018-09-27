# Generated by Django 2.0.4 on 2018-09-27 04:34

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macTools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyversion',
            name='drive_pw',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='下载密码'),
        ),
        migrations.AlterField(
            model_name='historyversion',
            name='drive_type',
            field=models.IntegerField(choices=[(1, 'Mac'), (2, 'Microsoft'), (3, 'Linux')], default=1, help_text='系统类型', verbose_name='系统类型'),
        ),
        migrations.AlterField(
            model_name='historyversion',
            name='drive_url',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='下载链接'),
        ),
        migrations.AlterField(
            model_name='historyversion',
            name='language',
            field=models.CharField(choices=[('CH', '中文'), ('EN', '英文'), ('CHEN', '中英文'), ('MORE', '多国语言')], help_text='工具语言', max_length=100, verbose_name='语言'),
        ),
        migrations.AlterField(
            model_name='historyversion',
            name='version',
            field=models.CharField(max_length=100, verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='tools',
            name='cate',
            field=models.IntegerField(choices=[(1, '应用软件'), (2, 'Sketch插件'), (3, '网络工具'), (4, '开发工具'), (5, '设计工具'), (6, '行业软件'), (7, '安全防护'), (8, '系统工具'), (9, '免费精品'), (10, '其他')], help_text='工具类别', verbose_name='工具类别'),
        ),
        migrations.AlterField(
            model_name='tools',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容\t'),
        ),
    ]
