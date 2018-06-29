# Generated by Django 2.0.6 on 2018-06-28 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BrowserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_count', models.IntegerField()),
                ('fail_count', models.IntegerField()),
                ('skip_count', models.IntegerField()),
                ('defects', models.CharField(max_length=100)),
                ('rca', models.CharField(max_length=2000)),
                ('action_plan', models.CharField(max_length=1000)),
                ('hostname', models.CharField(max_length=50)),
                ('report_path', models.URLField()),
                ('browser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='run_results.Browser')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_date', models.DateTimeField(verbose_name='run time and date')),
                ('overall_status', models.CharField(max_length=20)),
                ('suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='run_results.Suite')),
            ],
        ),
        migrations.AddField(
            model_name='browserreport',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='run_results.Reviewer'),
        ),
    ]