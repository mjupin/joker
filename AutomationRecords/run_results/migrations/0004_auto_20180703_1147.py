# Generated by Django 2.0.6 on 2018-07-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run_results', '0003_auto_20180628_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browserreport',
            name='defects',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
