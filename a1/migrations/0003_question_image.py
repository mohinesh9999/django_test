# Generated by Django 2.2.2 on 2020-01-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_auto_20200113_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.FileField(default='Images/None/NO_img.jpg', upload_to='Images/'),
        ),
    ]