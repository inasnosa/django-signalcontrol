# Generated by Django 2.2.12 on 2020-04-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignalControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=32)),
                ('model_name', models.CharField(max_length=128)),
                ('signal_name', models.CharField(max_length=255)),
                ('signal_type', models.CharField(max_length=32)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'signalcontrol',
                'unique_together': {('app_name', 'model_name', 'signal_name')},
            },
        ),
    ]
