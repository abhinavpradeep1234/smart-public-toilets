# Generated by Django 5.0.1 on 2024-01-03 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='searchtoilets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('s_status', models.CharField(max_length=200)),
                ('s_rate', models.CharField(max_length=200)),
                ('s_image', models.ImageField(upload_to='search')),
                ('s_serial', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('s_phone', models.CharField(max_length=10)),
                ('s_email', models.EmailField(max_length=254)),
                ('r_report', models.CharField(max_length=255)),
                ('s_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleankeralas.searchtoilets')),
            ],
        ),
    ]
