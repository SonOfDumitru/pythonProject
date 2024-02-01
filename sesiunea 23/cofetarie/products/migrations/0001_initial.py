# Generated by Django 4.2.9 on 2024-01-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('price', models.FloatField()),
            ],
        ),
    ]
