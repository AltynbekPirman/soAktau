# Generated by Django 2.1.1 on 2018-10-27 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_city', '0007_citynews_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='citynews',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='my_city_thumbnails'),
        ),
    ]
