# Generated by Django 3.1.3 on 2020-11-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_auto_20201112_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='currentorders',
            name='id',
        ),
        migrations.AlterField(
            model_name='currentorders',
            name='order_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
