# Generated by Django 4.2.3 on 2023-08-23 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_alter_client_detail_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('handle_by', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=80)),
                ('phone', models.IntegerField()),
                ('account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=20)),
                ('gst_number', models.CharField(max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.client_detail')),
            ],
        ),
    ]
