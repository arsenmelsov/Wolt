# Generated by Django 4.2.3 on 2023-08-01 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ReccomendedFood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reccomendedfood',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ea20c97b-b956-4146-978f-942c5f3e4905'), editable=False, primary_key=True, serialize=False),
        ),
    ]
