# Generated by Django 2.2.5 on 2019-09-17 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_realname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='realname',
        ),
    ]
