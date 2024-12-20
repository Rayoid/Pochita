# Generated by Django 5.1.3 on 2024-11-18 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0001_initial'),
        ('users', '0003_alter_client_id_alter_vet_id_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='pet_name',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.pet'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.client'),
        ),
    ]
