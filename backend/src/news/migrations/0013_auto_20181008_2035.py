# Generated by Django 2.1.1 on 2018-10-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_announcement_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='language',
        ),
        migrations.RemoveField(
            model_name='news',
            name='photo_url',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
        migrations.AddField(
            model_name='news',
            name='icon',
            field=models.ImageField(default='news_images/icon.png', upload_to='news_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='text_kaz',
            field=models.TextField(default='text', verbose_name='текст(kaz)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='text_rus',
            field=models.TextField(default='text', verbose_name='текст(rus)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title_kaz',
            field=models.TextField(default='title', verbose_name='название(kaz)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title_rus',
            field=models.TextField(default='title', verbose_name='название(rus)'),
            preserve_default=False,
        ),
    ]
