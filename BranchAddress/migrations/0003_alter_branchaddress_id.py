# Generated by Django 4.2.3 on 2023-08-02 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BranchAddress', '0002_alter_branchaddress_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchaddress',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dbb9d3e8-8c65-4700-9cb1-1c75459c3324'), editable=False, primary_key=True, serialize=False),
        ),
    ]
