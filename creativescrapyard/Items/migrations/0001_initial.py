# Generated by Django 3.1.4 on 2021-02-19 15:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CustomAdmin', '0004_auto_20210218_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_creativeitems_details',
            fields=[
                ('crt_item_details_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('crt_item_color', models.CharField(max_length=7)),
                ('crt_item_size', models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, null=True)),
                ('crt_item_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('crt_item_qty', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('crt_item_SKU', models.CharField(max_length=16, unique=True)),
                ('crt_item_status', models.CharField(choices=[('INAPPROPRIATE', 'Inappropriate'), ('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('SOLD', 'Sold')], default='ACTIVE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_scrapitems',
            fields=[
                ('scp_item_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('scp_item_name', models.CharField(max_length=100)),
                ('scp_item_desc', models.TextField()),
                ('scp_item_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('scp_item_qty', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('scp_item_SKU', models.CharField(max_length=16, unique=True)),
                ('scp_item_status', models.CharField(choices=[('INAPPROPRIATE', 'Inappropriate'), ('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('SOLD', 'Sold')], default='ACTIVE', max_length=20)),
                ('scp_created_on', models.DateTimeField(auto_now_add=True)),
                ('scp_last_modified', models.DateTimeField(auto_now_add=True)),
                ('scp_sub_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='CustomAdmin.subscrapcategory')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_scrapimages',
            fields=[
                ('scp_img_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('scp_img_url', models.ImageField(max_length=150, null=True, upload_to='item-photos/', validators=[django.core.validators.validate_image_file_extension])),
                ('is_primary', models.BooleanField(default=False)),
                ('scp_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.tbl_scrapitems')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_crtimages',
            fields=[
                ('crt_img_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('crt_img_url', models.ImageField(max_length=150, null=True, upload_to='item-photos/', validators=[django.core.validators.validate_image_file_extension])),
                ('is_primary', models.BooleanField(default=False)),
                ('crt_item_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.tbl_creativeitems_details')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_creativeitems_mst',
            fields=[
                ('crt_item_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('crt_item_name', models.CharField(max_length=100)),
                ('crt_item_desc', models.TextField()),
                ('crt_item_weight', models.CharField(blank=True, choices=[('1', 'Below 100g'), ('2', 'Below 250g'), ('3', 'Below 500g'), ('4', 'Below 1kg'), ('5', 'Below 5kg')], max_length=1, null=True)),
                ('crt_item_height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('crt_item_width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('crt_created_on', models.DateTimeField(auto_now_add=True)),
                ('crt_last_modified', models.DateTimeField(auto_now_add=True)),
                ('crt_sub_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='CustomAdmin.tbl_crt_subcategories')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_creativeitems_details',
            name='crt_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.tbl_creativeitems_mst'),
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('issue_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('issue_type', models.PositiveIntegerField(choices=[(1, 'Reported Creative Items'), (2, 'Reported Scrap Items'), (3, 'Reported Users Items')])),
                ('issue_sub', models.PositiveIntegerField(choices=[(1, "Doesn't match product"), (2, 'Missing/Incorrect information'), (3, 'Offensive or adult content'), (4, 'Is not clear'), (5, 'Other')])),
                ('issue_msg', models.TextField(blank=True, max_length=100, null=True)),
                ('issue_status', models.PositiveIntegerField(choices=[(1, 'Pending'), (2, 'Resolved'), (3, 'Rejected')], default=1)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('crt_item', models.PositiveIntegerField(blank=True, null=True)),
                ('scp_item', models.PositiveIntegerField(blank=True, null=True)),
                ('reported_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reportee', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_issues',
            },
        ),
    ]
