# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('83c26b0f-928a-4f04-9754-91afec8a192b'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Country.country')),
            ],
        ),
    ]
