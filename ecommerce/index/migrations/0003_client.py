# Generated by Django 4.2 on 2023-05-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='client/')),
            ],
        ),
    ]
