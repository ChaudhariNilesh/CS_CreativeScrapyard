# Generated by Django 3.1.4 on 2021-03-04 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0003_payment_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='order_id',
            new_name='order',
        ),
    ]
