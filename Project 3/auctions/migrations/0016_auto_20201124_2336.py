# Generated by Django 3.0.8 on 2020-11-24 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201124_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Item_category', to='auctions.Category'),
        ),
    ]
