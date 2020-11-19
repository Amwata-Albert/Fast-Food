# Generated by Django 3.1.3 on 2020-11-18 08:32


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('food_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('photo', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('order_id', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('order_timestamp', models.DateTimeField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Food.meals')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Food.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentOrders',
            fields=[
                ('quantity', models.IntegerField(null=True)),
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20, null=True)),
                ('order_timestamp', models.DateTimeField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Food.meals')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Food.customer')),
            ],
        ),
    ]
