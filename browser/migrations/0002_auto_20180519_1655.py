# Generated by Django 2.0.2 on 2018-05-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='previewImgPath',
            field=models.ImageField(upload_to=''),
        ),
    ]
