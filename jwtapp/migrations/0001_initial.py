# Generated by Django 2.1 on 2019-07-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(max_length=10)),
                ('username', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
    ]
