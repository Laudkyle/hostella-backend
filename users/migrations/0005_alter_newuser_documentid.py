# Generated by Django 4.1.7 on 2023-03-06 11:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_newuser_documentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='documentId',
            field=models.UUIDField(default=uuid.UUID('6d5bd400-4a8c-4c5a-8cf6-4fd68496a43a'), editable=False, null=True, unique=True),
        ),
    ]
