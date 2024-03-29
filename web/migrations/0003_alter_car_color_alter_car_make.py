# Generated by Django 4.1.3 on 2022-12-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_car_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'), ('Purple', 'Purple'), ('White', 'White'), ('Black', 'Black'), ('Gray', 'Gray')], max_length=6),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Ferrari', 'Ferrari'), ('BMW', 'Bmw'), ('Mercedes', 'Mercedes'), ('Lamborghini', 'Lamborghini'), ('Porsche', 'Porsche'), ('Audi', 'Audi'), ('Tesla', 'Tesla'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia')], max_length=30),
        ),
    ]
