# Generated by Django 2.1.1 on 2018-10-11 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_default_langs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('buses', models.CharField(max_length=256, verbose_name='автобусы')),
            ],
            options={
                'verbose_name': 'адрес',
                'verbose_name_plural': 'адрес',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_kaz', models.TextField()),
                ('info_rus', models.TextField()),
            ],
            options={
                'verbose_name': 'О Компании',
                'verbose_name_plural': 'О Компании',
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=20, verbose_name='долгота(карта)')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=20, verbose_name='широта(карта)')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinates', to='main.Address', verbose_name='адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=64, verbose_name='телефон')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phones', to='main.Address', verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'телефон',
                'verbose_name_plural': 'телефон',
            },
        ),
    ]
