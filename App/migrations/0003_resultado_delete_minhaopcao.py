# Generated by Django 5.1.1 on 2024-09-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_minhaopcao_css_minhaopcao_java'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variavel1', models.BooleanField(default=False)),
                ('variavel2', models.BooleanField(default=False)),
                ('variavel3', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='MinhaOpcao',
        ),
    ]