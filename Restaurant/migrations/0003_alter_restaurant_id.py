# Generated by Django 4.2.3 on 2023-08-02 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_alter_restaurant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f07b9c48-35bf-4781-9b19-e43f9a1c1ba2'), editable=False, primary_key=True, serialize=False),
        ),
    ]
