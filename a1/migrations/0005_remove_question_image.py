# Generated by Django 2.2.2 on 2020-01-17 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0004_auto_20200113_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]