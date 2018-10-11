# Generated by Django 2.1.1 on 2018-10-11 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181011_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_kaz', models.TextField()),
                ('message_rus', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_rus', models.CharField(max_length=512, verbose_name='Название чата(kaz)')),
                ('title_kaz', models.CharField(max_length=512, verbose_name='Название чата(rus)')),
            ],
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='main.ChatRoom'),
        ),
    ]