# Generated by Django 4.2.3 on 2024-03-14 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address', models.CharField(default='', max_length=255)),
                ('order_description', models.TextField(default='')),
                ('is_complete', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
        ),
    ]
