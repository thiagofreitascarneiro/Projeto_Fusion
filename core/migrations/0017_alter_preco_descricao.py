# Generated by Django 3.2.6 on 2021-09-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_preco_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preco',
            name='descricao',
            field=models.TextField(max_length=450, verbose_name='Descrição'),
        ),
    ]
