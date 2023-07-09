# Generated by Django 4.2.3 on 2023-07-09 20:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Card', '0001_initial'),
        ('Users', '0005_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('38e2c054-f6e1-4d48-be54-67b26af9d271'), editable=False, primary_key=True, serialize=False)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Card.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
    ]
