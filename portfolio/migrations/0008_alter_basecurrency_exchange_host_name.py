# Generated by Django 3.2.10 on 2021-12-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_basecurrency_exchange_host_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecurrency',
            name='exchange_host_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='exchange_host_name'),
        ),
    ]
