# Generated by Django 2.0.2 on 2018-03-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0012_auto_20180304_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Kvantitet'),
        ),
    ]