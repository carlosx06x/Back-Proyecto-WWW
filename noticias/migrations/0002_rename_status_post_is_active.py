# Generated by Django 4.1.4 on 2022-12-29 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='status',
            new_name='is_active',
        ),
    ]
