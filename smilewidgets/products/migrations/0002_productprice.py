# Generated by Django 2.0.7 on 2019-09-17 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('new_price', models.PositiveIntegerField(help_text='New price of product in cents')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='products.Product')),
            ],
        ),
    ]
