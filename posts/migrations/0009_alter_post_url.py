# Generated by Django 3.2 on 2021-04-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=500, null=True, unique=True),
        ),
    ]
