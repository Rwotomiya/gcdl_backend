# Generated by Django 5.2 on 2025-04-09 12:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('company', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tonnage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('branch', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.dealer')),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.produce')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_tonnage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.produce')),
            ],
        ),
    ]
