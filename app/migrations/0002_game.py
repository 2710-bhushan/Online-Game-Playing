# Generated by Django 5.0.6 on 2024-07-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameimagelink', models.CharField(max_length=30)),
                ('gamename', models.CharField(max_length=40)),
                ('gamedate', models.DateField()),
                ('description', models.TextField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('link1', models.CharField(max_length=10)),
            ],
        ),
    ]
