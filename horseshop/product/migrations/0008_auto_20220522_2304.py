# Generated by Django 3.2 on 2022-05-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220522_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productincart',
            name='property',
        ),
        migrations.AddField(
            model_name='productincart',
            name='color',
            field=models.CharField(choices=[('BK', 'Black'), ('WT', 'White'), ('BL', 'Blue'), ('BR', 'Brown'), ('RD', 'Red'), ('GR', 'Green')], default='BK', max_length=2),
        ),
        migrations.AddField(
            model_name='productincart',
            name='gender',
            field=models.CharField(choices=[('C', 'Child'), ('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='productincart',
            name='size',
            field=models.PositiveIntegerField(choices=[(38, '38'), (40, '40'), (42, '42'), (44, '44'), (46, '46'), (120, '120'), (130, '130'), (140, '140'), (150, '150'), (160, '160')], default=38),
        ),
    ]