# Generated by Django 4.1.1 on 2022-09-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='home/static/img/team'),
        ),
    ]
