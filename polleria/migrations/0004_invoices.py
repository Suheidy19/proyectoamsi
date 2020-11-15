# Generated by Django 3.1.2 on 2020-10-28 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polleria', '0003_auto_20201028_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=20, verbose_name='Fecha de factura')),
                ('Total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total de la venta')),
                ('Name_Clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polleria.clients', verbose_name='Nombre Cliente')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
