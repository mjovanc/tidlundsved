# Generated by Django 2.0.2 on 2018-03-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0003_auto_20180302_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='firewood_type',
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='product_type',
            field=models.CharField(choices=[(1, 'Blandat lövträd'), (2, 'Björkved'), (3, 'Bokved'), (4, 'Askved'), (5, 'Övrigt')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]