# Generated by Django 2.1.1 on 2018-10-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181012_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='icon',
            field=models.ImageField(default='chat_icons/icon.png', upload_to='chat_icons'),
            preserve_default=False,
        ),
    ]