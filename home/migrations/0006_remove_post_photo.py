# Generated by Django 4.1.4 on 2022-12-29 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_body_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]