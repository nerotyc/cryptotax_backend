# Generated by Django 3.1.7 on 2021-12-26 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax_analysis', '0015_auto_20211226_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysisconsumable',
            name='amount',
        ),
    ]
