# Generated by Django 4.1.7 on 2023-03-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_contactus_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
