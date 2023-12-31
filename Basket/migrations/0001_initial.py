# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('7b5a76b5-84fe-4c21-a164-f02e73f7ce3d'), editable=False, primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
                ('arrival_time', models.TimeField()),
                ('rating', models.FloatField()),
                ('payment_status', models.BooleanField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courier.courier')),
            ],
        ),
    ]
