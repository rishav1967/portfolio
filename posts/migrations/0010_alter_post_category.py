# Generated by Django 3.2 on 2021-04-26 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Category'),
        ),
    ]
