# Generated by Django 4.1.7 on 2023-03-08 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopaccount', '0007_payouttype_payout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payout',
            old_name='date',
            new_name='pay_date',
        ),
    ]