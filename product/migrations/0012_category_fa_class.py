# Generated by Django 3.0.8 on 2020-07-29 22:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='fa_class',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]