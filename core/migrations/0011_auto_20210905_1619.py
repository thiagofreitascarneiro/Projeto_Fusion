# Generated by Django 3.2.6 on 2021-09-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_preco_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preco',
            name='categoria',
            field=models.CharField(choices=[('a', 'Premium'), ('b', 'Pro'), ('c', 'Plus')], max_length=15, verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='preco',
            name='descricao',
            field=models.TextField(max_length=150, verbose_name='Descrição'),
        ),
    ]
