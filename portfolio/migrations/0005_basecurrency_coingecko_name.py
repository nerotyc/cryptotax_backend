# Generated by Django 3.2.10 on 2021-12-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_basecurrency_coingecko_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecurrency',
            name='coingecko_name',
            field=models.CharField(default='EUR', max_length=150, verbose_name='coingecko_name'),
            preserve_default=False,
        ),
    ]
