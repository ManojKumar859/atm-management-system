# Generated by Django 4.0.1 on 2022-05-25 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0003_atm_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='relate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm.bankname'),
        ),
    ]
