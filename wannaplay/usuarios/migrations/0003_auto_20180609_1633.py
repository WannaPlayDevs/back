# Generated by Django 2.0.4 on 2018-06-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20180527_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
