# Generated by Django 3.0.3 on 2021-10-19 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filtros', '0007_auto_20211019_0312'),
        ('testes', '0006_auto_20211018_1508'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Upload',
        ),
        migrations.RemoveField(
            model_name='image',
            name='action',
        ),
    ]
