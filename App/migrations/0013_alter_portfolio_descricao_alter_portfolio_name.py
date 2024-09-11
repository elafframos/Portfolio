# Generated by Django 5.1.1 on 2024-09-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_portfolio_name_alter_portfolio_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='descricao',
            field=models.CharField(blank=True, max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Nome do Projeto'),
        ),
    ]
