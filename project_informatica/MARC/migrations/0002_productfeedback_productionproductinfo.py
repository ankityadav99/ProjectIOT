# Generated by Django 2.1.7 on 2019-03-16 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('services', models.TextField()),
                ('product_quality', models.CharField(max_length=100)),
                ('suggestions', models.CharField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], max_length=10)),
                ('future_scope', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductionProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField()),
                ('name_of_product', models.CharField(max_length=100)),
                ('type_of_product', models.CharField(max_length=100)),
                ('firmware_version', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('customer_id', models.CharField(max_length=50)),
                ('last_Upgraded', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('validity', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('alarms', models.TextField()),
                ('health', models.IntegerField()),
                ('auto_recovery', models.IntegerField()),
                ('last_rebooted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('system_crash_report', models.TextField()),
                ('security', models.CharField(max_length=150)),
                ('authority', models.CharField(max_length=100)),
            ],
        ),
    ]