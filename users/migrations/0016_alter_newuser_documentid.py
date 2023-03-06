# Generated by Django 4.1.7 on 2023-03-06 12:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_newuser_documentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='documentId',
            field=models.UUIDField(default=uuid.UUID('98943cdd-25e4-44ad-b80c-b0c6635e3889'), editable=False, null=True, unique=True),
        ),
    ]