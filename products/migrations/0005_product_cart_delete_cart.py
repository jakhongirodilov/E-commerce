# Generated by Django 4.2.3 on 2023-07-05 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]