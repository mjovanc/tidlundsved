# Generated by Django 2.0.2 on 2018-03-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0004_auto_20180302_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_type',
            field=models.CharField(choices=[('Blandat lövträd', 'Blandat lövträd'), ('Björkved', 'Björkved'), ('Bokved', 'Bokved'), ('Askved', 'Askved'), ('Övrigt', 'Övrigt')], default=1, max_length=50),
        ),
    ]
