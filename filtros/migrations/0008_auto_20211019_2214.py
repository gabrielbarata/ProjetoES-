# Generated by Django 3.0.3 on 2021-10-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtros', '0007_auto_20211019_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='codigo',
            field=models.TextField(help_text='image_in e image_out são arrays numpy.\n    atribua o valor da variavel image_out a partir de image_in.', max_length=255, verbose_name='Código'),
        ),
    ]
