# Generated by Django 3.0.4 on 2020-03-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_auto_20200310_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='offerprice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='userid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
