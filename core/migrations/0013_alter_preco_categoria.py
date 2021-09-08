# Generated by Django 3.2.6 on 2021-09-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_preco_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preco',
            name='categoria',
            field=models.CharField(choices=[('Plus', 'A'), ('Pro', 'B'), ('Premium', 'C')], max_length=15, verbose_name='categoria'),
        ),
    ]