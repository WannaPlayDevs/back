# Generated by Django 2.0.4 on 2018-05-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('pkUser', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=25)),
                ('userpass', models.TextField(max_length=25)),
                ('alias', models.TextField(max_length=25)),
                ('karma', models.IntegerField(default=0)),
                ('steamName', models.TextField()),
                ('bnetName', models.TextField()),
                ('horarioManana', models.BooleanField(default=False)),
                ('horarioTarde', models.BooleanField(default=False)),
                ('horarioNoche', models.BooleanField(default=False)),
                ('horarioMadrugada', models.BooleanField(default=False)),
                ('playOverwatch', models.BooleanField(default=False)),
                ('playWow', models.BooleanField(default=False)),
                ('playRust', models.BooleanField(default=False)),
                ('playArk', models.BooleanField(default=False)),
                ('playGta', models.BooleanField(default=False)),
                ('playPubg', models.BooleanField(default=False)),
                ('playFortnite', models.BooleanField(default=False)),
            ],
        ),
    ]
