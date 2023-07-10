# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('f2fda93e-8975-4d3e-b984-2d5171fb7825'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
