# Generated by Django 5.1.1 on 2024-09-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minhaopcao',
            name='css',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='minhaopcao',
            name='java',
            field=models.BooleanField(default=False),
        ),
    ]
