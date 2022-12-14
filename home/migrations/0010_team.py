# Generated by Django 4.1.1 on 2022-09-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_service_icons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='team_pictures/')),
                ('twitter', models.CharField(default='#', max_length=200)),
                ('facebook', models.CharField(default='#', max_length=200)),
                ('instagram', models.CharField(default='#', max_length=200)),
                ('linkedin', models.CharField(default='#', max_length=200)),
            ],
        ),
    ]
