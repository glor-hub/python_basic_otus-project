# Generated by Django 3.2 on 2022-05-22 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20220522_2304'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductInCartProperty',
        ),
    ]
