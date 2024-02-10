# Generated by Django 5.0.1 on 2024-02-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_license_orders', '0006_remove_driverlicenseorder_renewal_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverlicenseorder',
            name='status',
            field=models.CharField(choices=[('WAITING_APPROVAL', 'Waiting Approval'), ('PENDING', 'Pending'), ('DONE', 'Done'), ('REJECTED', 'Rejected'), ('CANCELED', 'Canceled')], default='WAITING_APPROVAL', max_length=32, null=True),
        ),
    ]
