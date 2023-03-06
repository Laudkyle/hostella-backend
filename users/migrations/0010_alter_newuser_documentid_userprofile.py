# Generated by Django 4.1.7 on 2023-03-06 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_newuser_documentid_alter_newuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='documentId',
            field=models.UUIDField(default=uuid.UUID('5bb5da91-55e1-4d4c-9b79-8b337194fb10'), editable=False, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_Name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('phoneNumber', models.CharField(max_length=200, null=True)),
                ('level', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]