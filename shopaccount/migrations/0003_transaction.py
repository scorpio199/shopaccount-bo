# Generated by Django 4.1.7 on 2023-02-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopaccount', '0002_remove_marketplace_mp_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('order_id', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_category', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('basic_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('mp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopaccount.marketplace')),
            ],
        ),
    ]
