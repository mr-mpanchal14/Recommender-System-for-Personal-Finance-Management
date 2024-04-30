# Generated by Django 5.0.3 on 2024-03-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.BinaryField()),
                ('education', models.CharField(max_length=100)),
                ('income', models.IntegerField()),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
