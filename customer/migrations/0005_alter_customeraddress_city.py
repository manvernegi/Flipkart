# Generated by Django 4.2.1 on 2023-05-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customers_age_alter_customers_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
