# Generated by Django 3.1.7 on 2021-12-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_analysis', '0013_delete_analysissdepositconsumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioanalysis',
            name='algo',
            field=models.CharField(choices=[('FIFO', 'ALGO_FIFO'), ('LIFO', 'ALGO_LIFO'), ('OPT', 'ALGO_OPTIMAL'), ('WRST', 'ALGO_WORST')], default='FIFO', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioanalysis',
            name='transfer_algo',
            field=models.CharField(choices=[('FIFO', 'ALGO_FIFO'), ('LIFO', 'ALGO_LIFO'), ('OPT', 'ALGO_OPTIMAL'), ('WRST', 'ALGO_WORST')], default='FIFO', max_length=5),
            preserve_default=False,
        ),
    ]
