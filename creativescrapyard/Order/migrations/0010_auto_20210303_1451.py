# Generated by Django 3.1.4 on 2021-03-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_auto_20210303_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_orders_mst',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]