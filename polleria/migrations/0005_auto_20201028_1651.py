# Generated by Django 3.1.2 on 2020-10-28 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polleria', '0004_invoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='Date',
            field=models.DateField(verbose_name='Fecha de factura'),
        ),
    ]
