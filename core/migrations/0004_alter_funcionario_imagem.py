# Generated by Django 3.2.6 on 2021-09-02 14:20

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='equipe', verbose_name='Imagem'),
        ),
    ]
