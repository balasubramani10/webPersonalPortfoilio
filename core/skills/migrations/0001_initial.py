# Generated by Django 5.0.3 on 2024-03-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBackEndSKills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('icon', models.ImageField(upload_to='skills_icons')),
            ],
        ),
        migrations.CreateModel(
            name='MyFrontEndSKills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('icon', models.ImageField(upload_to='skills_icons')),
            ],
        ),
    ]
