# Generated by Django 3.1.7 on 2021-12-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax_analysis', '0016_remove_analysisconsumable_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysisconsumable',
            name='exchange_wallet',
        ),
    ]