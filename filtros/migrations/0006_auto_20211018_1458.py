# Generated by Django 3.0.3 on 2021-10-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtros', '0005_alter_script_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teste',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
