# Generated by Django 3.0.4 on 2020-03-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
