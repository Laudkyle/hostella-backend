# Generated by Django 4.1.7 on 2023-03-06 12:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_newuser_last_name_alter_newuser_documentid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='documentId',
            field=models.UUIDField(default=uuid.UUID('35a533c3-701f-4d34-af88-b8177d77d9ed'), editable=False, null=True, unique=True),
        ),
    ]