# Generated by Django 4.0.3 on 2022-04-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_n_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='eaten',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grocery',
            name='min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grocery',
            name='nowHave',
            field=models.IntegerField(default=0),
        ),
    ]
