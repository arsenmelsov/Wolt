# Generated by Django 4.2.3 on 2023-08-02 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ReccomendedFood', '0002_alter_reccomendedfood_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reccomendedfood',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b78311ad-859b-4fa6-9910-199c5b053a8e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
