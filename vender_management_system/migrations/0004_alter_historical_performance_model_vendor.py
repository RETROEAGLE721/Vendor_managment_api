# Generated by Django 4.2.7 on 2023-11-26 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vender_management_system', '0003_remove_historical_performance_model_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historical_performance_model',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='vender_management_system.vendor_model', unique=True),
        ),
    ]
