# Generated by Django 5.0.1 on 2024-02-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_license_orders', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverlicenseorder',
            name='governorate',
        ),
        migrations.AddField(
            model_name='driverlicenseorder',
            name='installment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='driverlicenseorder',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='driverlicenseorder',
            name='status',
            field=models.CharField(choices=[('WAITINGAPPROVAL', 'Waitingapproval'), ('PENDING', 'Pending'), ('DONE', 'Done'), ('REJECTED', 'Rejected')], default='WAITINGAPPROVAL', max_length=32, null=True),
        ),
    ]
