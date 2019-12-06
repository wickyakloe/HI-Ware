# Generated by Django 3.0 on 2019-12-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
    ]
