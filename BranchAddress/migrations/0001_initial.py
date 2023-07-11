# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('8ff7227a-7eb1-4107-a888-64cece57bbab'), editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=50)),
                ('house', models.IntegerField()),
            ],
        ),
    ]