# Generated by Django 4.1.1 on 2022-09-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description_text',
            field=models.CharField(max_length=200),
        ),
    ]