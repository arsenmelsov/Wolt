# Generated by Django 4.2.3 on 2023-08-01 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.UUIDField(default=uuid.UUID('609d0804-0759-4d67-8c98-a596aa8f462f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
