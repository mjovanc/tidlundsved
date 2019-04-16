# Generated by Django 2.0.2 on 2018-03-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0009_auto_20180302_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='firewood_choice',
            field=models.CharField(max_length=50, verbose_name='Val'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Ej påbörjad', 'Ej påbörjad'), ('Påbörjad', 'Påbörjad'), ('Levererad', 'Levererad')], default='Ej påbörjad', max_length=30, verbose_name='Status på order'),
        ),
    ]
