# Generated by Django 4.0.3 on 2022-04-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_n_shop', '0002_grocery_eaten_grocery_min_grocery_nowhave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='eaten',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='min',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='nowHave',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
