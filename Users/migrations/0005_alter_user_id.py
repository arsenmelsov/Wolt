# Generated by Django 4.2.3 on 2023-07-09 20:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5a2d50a1-cbc3-49fb-bb4a-4188f4771891'), editable=False, primary_key=True, serialize=False),
        ),
    ]
