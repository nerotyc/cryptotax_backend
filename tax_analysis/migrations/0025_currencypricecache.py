# Generated by Django 3.1.7 on 2022-01-04 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20211228_1415'),
        ('tax_analysis', '0024_analysisconsumable_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPriceCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.basecurrency')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.currency')),
            ],
        ),
    ]
