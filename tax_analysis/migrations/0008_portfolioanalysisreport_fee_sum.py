# Generated by Django 3.2.10 on 2021-12-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_analysis', '0007_portfolioanalysis_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioanalysisreport',
            name='fee_sum',
            field=models.FloatField(default=0, verbose_name='fee_sum'),
        ),
    ]
