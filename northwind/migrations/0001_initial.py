# Generated by Django 4.0.1 on 2022-01-30 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40)),
                ('contact_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_title', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('region', models.CharField(blank=True, max_length=15, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
                ('fax', models.CharField(blank=True, max_length=24, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=10)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('title_of_courtesy', models.CharField(blank=True, max_length=25, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('region', models.CharField(blank=True, max_length=15, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=24, null=True)),
                ('extension', models.CharField(blank=True, max_length=4, null=True)),
                ('photo', models.BinaryField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('photo_path', models.CharField(blank=True, max_length=255, null=True)),
                ('reports_to', models.ForeignKey(blank=True, db_column='reports_to', null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.employee')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('region_description', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('shipper_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
            ],
            options={
                'db_table': 'shippers',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40)),
                ('contact_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_title', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('region', models.CharField(blank=True, max_length=15, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
                ('fax', models.CharField(blank=True, max_length=24, null=True)),
                ('homepage', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='UsState',
            fields=[
                ('state_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=100, null=True)),
                ('state_abbr', models.CharField(blank=True, max_length=2, null=True)),
                ('state_region', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'us_states',
            },
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('territory_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('territory_description', models.CharField(max_length=30)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='northwind.region')),
            ],
            options={
                'verbose_name_plural': 'territories',
                'db_table': 'territories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=40)),
                ('quantity_per_unit', models.CharField(blank=True, max_length=20, null=True)),
                ('unit_price', models.FloatField(blank=True, null=True)),
                ('units_in_stock', models.SmallIntegerField(blank=True, null=True)),
                ('units_on_order', models.SmallIntegerField(blank=True, null=True)),
                ('reorder_level', models.SmallIntegerField(blank=True, null=True)),
                ('discontinued', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.category')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='northwind.supplier')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('required_date', models.DateField(blank=True, null=True)),
                ('shipped_date', models.DateField(blank=True, null=True)),
                ('freight', models.FloatField(blank=True, null=True)),
                ('ship_name', models.CharField(blank=True, max_length=40, null=True)),
                ('ship_address', models.CharField(blank=True, max_length=60, null=True)),
                ('ship_city', models.CharField(blank=True, max_length=15, null=True)),
                ('ship_region', models.CharField(blank=True, max_length=15, null=True)),
                ('ship_postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('ship_country', models.CharField(blank=True, max_length=15, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.customer')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.employee')),
                ('ship_via', models.ForeignKey(blank=True, db_column='ship_via', null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.shipper')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='territories',
            field=models.ManyToManyField(to='northwind.Territory'),
        ),
        migrations.CreateModel(
            name='CustomerDemographic',
            fields=[
                ('customer_type_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('customer_desc', models.TextField(blank=True, null=True)),
                ('customers', models.ManyToManyField(to='northwind.Customer')),
            ],
            options={
                'db_table': 'customer_demographics',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.FloatField()),
                ('quantity', models.SmallIntegerField()),
                ('discount', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='northwind.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.product')),
            ],
            options={
                'db_table': 'order_details',
                'unique_together': {('order', 'product')},
            },
        ),
    ]
