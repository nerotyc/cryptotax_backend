# Generated by Django 3.1.7 on 2021-12-31 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tax_analysis', '0022_auto_20211228_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysistransferconsumer',
            name='consumer',
        ),
        migrations.AddField(
            model_name='analysistransferconsumer',
            name='created_consumable',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='tax_analysis.analysisconsumable'),
            preserve_default=False,
        ),
    ]
