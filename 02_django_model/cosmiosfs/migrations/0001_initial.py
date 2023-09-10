# Generated by Django 4.2.5 on 2023-09-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('about', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='students')),
            ],
        ),
    ]
