# Generated by Django 4.2.3 on 2023-08-01 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5133bd1c-292c-44c7-96ca-5352b159dc4b'), editable=False, primary_key=True, serialize=False),
        ),
    ]