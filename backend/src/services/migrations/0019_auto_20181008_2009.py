# Generated by Django 2.1.1 on 2018-10-08 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20181007_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calcparameter',
            options={'verbose_name': 'параметр(Калькулятор)', 'verbose_name_plural': 'параметры(Калькулятор)'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': ' Услуга', 'verbose_name_plural': ' Услуги'},
        ),
        migrations.AlterModelOptions(
            name='subservice',
            options={'verbose_name': ' Суб-Услуги', 'verbose_name_plural': ' Суб-Услуги'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': ' Заглавие', 'verbose_name_plural': ' Заглавие'},
        ),
    ]