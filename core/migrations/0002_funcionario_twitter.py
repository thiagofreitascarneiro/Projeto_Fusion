# Generated by Django 3.2.6 on 2021-09-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='twitter',
            field=models.CharField(default='#', max_length=100, verbose_name='Twitter'),
        ),
    ]