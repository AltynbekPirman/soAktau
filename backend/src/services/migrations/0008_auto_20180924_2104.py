# Generated by Django 2.1.1 on 2018-09-24 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20180924_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='services.Service', verbose_name='услуга'),
        ),
    ]
