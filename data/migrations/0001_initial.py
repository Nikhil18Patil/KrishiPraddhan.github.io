# Generated by Django 4.1.7 on 2023-03-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.TextField(max_length=400)),
            ],
        ),
    ]
