# Generated by Django 3.2.6 on 2021-11-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_data', '0003_auto_20211124_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='college_image/'),
        ),
    ]