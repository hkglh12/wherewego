# Generated by Django 2.2.1 on 2019-08-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('morpheme', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('score', models.IntegerField()),
                ('coord_latitude', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('coord_longitude', models.CharField(blank=True, default=' ', max_length=500, null=True)),
            ],
            options={
                'db_table': 'dic',
            },
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=500)),
                ('contents', models.TextField(blank=True, default=' ', null=True)),
                ('url', models.TextField(blank=True, default=' ', null=True)),
            ],
            options={
                'db_table': 'rawdata',
            },
        ),
    ]