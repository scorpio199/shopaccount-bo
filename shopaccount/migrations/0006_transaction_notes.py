# Generated by Django 4.1.7 on 2023-02-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopaccount', '0005_alter_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='notes',
            field=models.TextField(default=-1.0, max_length=500),
            preserve_default=False,
        ),
    ]
