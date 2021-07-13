# Generated by Django 3.2.5 on 2021-07-12 07:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('prompt', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
