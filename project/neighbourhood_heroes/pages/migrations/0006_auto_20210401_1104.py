# Generated by Django 3.1.7 on 2021-04-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210401_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='Open', max_length=200),
        ),
    ]
