# Generated by Django 4.2.3 on 2023-08-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_alter_add_service_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_service',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
