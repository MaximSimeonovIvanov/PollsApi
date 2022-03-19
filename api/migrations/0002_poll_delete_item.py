# Generated by Django 4.0.3 on 2022-03-19 13:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
