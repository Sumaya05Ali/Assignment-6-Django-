# Generated by Django 5.1.3 on 2024-12-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('center', models.CharField(max_length=255)),
                ('parent_id', models.IntegerField()),
                ('location_type', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=2)),
                ('state_abbr', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]