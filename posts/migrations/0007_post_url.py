# Generated by Django 3.2 on 2021-04-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210424_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(null=True, unique=True),
        ),
    ]
