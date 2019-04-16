# Generated by Django 2.0.2 on 2018-03-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_option',
            field=models.CharField(choices=[(1, 'Hämta på plats'), (2, ())], default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='firewood_quantity',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
