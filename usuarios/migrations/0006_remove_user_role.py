# Generated by Django 4.1.4 on 2022-12-29 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
