# Generated by Django 2.2 on 2019-04-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0021_auto_20190419_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='ptype',
            field=models.CharField(choices=[('Blandat lövträd', 'Blandat lövträd'), ('Björkved', 'Björkved'), ('Bokved', 'Bokved'), ('Askved', 'Askved'), ('Övrigt', 'Övrigt')], default=1, max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
