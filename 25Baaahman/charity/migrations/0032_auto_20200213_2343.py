# Generated by Django 2.1.5 on 2020-02-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0031_auto_20200213_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='photo',
            field=models.ImageField(blank=True, upload_to='charity_Image'),
        ),
    ]
