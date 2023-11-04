# Generated by Django 4.2.4 on 2023-11-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0002_stock_stock_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manager', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='serial_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stock_category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
