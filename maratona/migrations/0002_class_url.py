# Generated by Django 3.0.8 on 2020-07-05 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maratona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='url',
            field=models.CharField(max_length=255, null=True, verbose_name='url'),
        ),
    ]
