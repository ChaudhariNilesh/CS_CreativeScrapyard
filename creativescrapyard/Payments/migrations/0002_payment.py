# Generated by Django 3.1.4 on 2021-03-02 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('transaction_id', models.CharField(max_length=50)),
                ('payment_mode', models.CharField(choices=[('PPI', 'Paytm Wallet'), ('UPI', 'UPI'), ('CC', 'Credit Card'), ('DC', 'Debit Card'), ('NB', 'Net Banking')], max_length=3)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_amt', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('payment_status', models.PositiveIntegerField(choices=[(1, 'Pending'), (2, 'Success'), (3, 'Failed')])),
                ('payment_remark', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_payments',
            },
        ),
    ]
