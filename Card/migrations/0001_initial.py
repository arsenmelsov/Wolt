# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('date', models.TextField()),
                ('cvv', models.TextField()),
            ],
        ),
    ]
