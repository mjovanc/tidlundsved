# Generated by Django 2.0.2 on 2018-03-04 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0010_auto_20180303_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='firewood_quantity',
            new_name='quantity',
        ),
    ]