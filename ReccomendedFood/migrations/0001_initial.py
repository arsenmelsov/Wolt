# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReccomendedFood',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3b785c67-298c-4ee4-85d3-df4bb69e67d1'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.food')),
            ],
        ),
    ]
