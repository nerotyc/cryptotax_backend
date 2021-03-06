# Generated by Django 3.2.10 on 2021-12-18 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('tag', models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='tag')),
                ('coingecko_name', models.CharField(max_length=150, verbose_name='coingecko_name')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='title')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='datetime')),
                ('type', models.CharField(choices=[('O', 'Order'), ('T', 'Transfer'), ('D', 'Deposit')], default='O', max_length=4)),
                ('exchange_wallet', models.TextField(blank=True, null=True, verbose_name='exchange_wallet')),
                ('fee', models.FloatField(default=0, verbose_name='fee')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('fee_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.currency')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_exchange_wallet', models.TextField(blank=True, null=True, verbose_name='from_exchange_wallet')),
                ('amount', models.FloatField(default=0, verbose_name='amount')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.currency')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_amount', models.FloatField(default=0, verbose_name='from_amount')),
                ('to_amount', models.FloatField(default=0, verbose_name='to_amount')),
                ('from_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_from_currency', to='portfolio.currency')),
                ('to_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_to_currency', to='portfolio.currency')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, verbose_name='amount')),
                ('taxable', models.FloatField(default=0, verbose_name='taxable')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.currency')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.transaction')),
            ],
        ),
    ]
