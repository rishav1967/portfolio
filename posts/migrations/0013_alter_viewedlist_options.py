# Generated by Django 3.2 on 2021-04-27 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_viewedlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewedlist',
            options={'ordering': ('-last_viewed',)},
        ),
    ]
