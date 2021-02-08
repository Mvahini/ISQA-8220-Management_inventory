# Generated by Django 3.1.6 on 2021-02-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20210204_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('start_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('cost_estimation', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
