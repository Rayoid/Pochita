# Generated by Django 5.1.3 on 2024-11-18 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='category',
            field=models.CharField(default='General', max_length=50),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='inventory_images/'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
