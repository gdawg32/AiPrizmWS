# Generated by Django 4.1.1 on 2022-09-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_service_description_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description_text',
            field=models.CharField(max_length=2000),
        ),
    ]
