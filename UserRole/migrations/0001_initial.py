# Generated by Django 4.2.3 on 2023-07-09 20:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0003_alter_user_id'),
        ('Role', '0002_alter_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e31f9320-f0f6-44c1-b11a-b4882626d6ee'), editable=False, primary_key=True, serialize=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Role.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
    ]
