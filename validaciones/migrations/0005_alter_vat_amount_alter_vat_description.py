# Generated by Django 4.0 on 2022-01-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validaciones', '0004_rename_amount_vat_validation_sale_vat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vat',
            name='description',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
