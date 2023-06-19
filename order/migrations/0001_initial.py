# Generated by Django 4.2.1 on 2023-06-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=32)),
                ('order_total', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=32)),
                ('delivery_options', models.CharField(max_length=32)),
                ('delivery_date', models.DateField()),
            ],
        ),
    ]
