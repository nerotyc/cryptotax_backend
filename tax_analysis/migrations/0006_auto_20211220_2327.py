# Generated by Django 3.2.10 on 2021-12-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_analysis', '0005_analysable_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysable',
            name='analysed',
            field=models.BooleanField(default=False, verbose_name='analysed'),
        ),
        migrations.AddField(
            model_name='portfolioanalysis',
            name='cooldown_until',
            field=models.DateTimeField(blank=True, null=True, verbose_name='cooldown_until'),
        ),
    ]
