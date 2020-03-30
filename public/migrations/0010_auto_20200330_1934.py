# Generated by Django 3.0.4 on 2020-03-30 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmers', '0014_auto_20200330_1934'),
        ('public', '0009_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='productid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='farmers.products'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='userid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='productid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='farmers.products'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='userid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='orderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('paymode', models.CharField(default=None, max_length=20)),
                ('productid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='farmers.products')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
