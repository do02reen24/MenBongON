# Generated by Django 2.1.8 on 2019-08-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('event_date', models.DateTimeField(verbose_name='event day')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QandA_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='QandA_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
    ]
