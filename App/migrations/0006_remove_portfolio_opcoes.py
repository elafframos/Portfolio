# Generated by Django 5.1.1 on 2024-09-03 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_portfolio_opcoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='opcoes',
        ),
    ]
