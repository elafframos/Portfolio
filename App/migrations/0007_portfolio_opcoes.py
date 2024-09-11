# Generated by Django 5.1.1 on 2024-09-03 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_remove_portfolio_opcoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='opcoes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='app_nome', to='App.resultado', verbose_name='Tecnologias'),
        ),
    ]