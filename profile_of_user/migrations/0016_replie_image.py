# Generated by Django 3.1.7 on 2021-06-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_of_user', '0015_auto_20210621_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='replie',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
