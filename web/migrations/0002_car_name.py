# Generated by Django 4.1.3 on 2022-12-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]