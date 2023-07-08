# Generated by Django 4.2.3 on 2023-07-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15)),
                ('body', models.TextField(blank=True)),
                ('autor', models.CharField(blank=True, max_length=15)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
