# Generated by Django 4.2.3 on 2023-07-10 13:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BranchAddress', '0001_initial'),
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3d2aac80-1298-41f9-8461-2ac350b0804d'), editable=False, primary_key=True, serialize=False)),
                ('radius', models.IntegerField()),
                ('rating', models.FloatField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BranchAddress.branchaddress')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.restaurant')),
            ],
        ),
    ]