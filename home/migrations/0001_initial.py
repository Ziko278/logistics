# Generated by Django 4.1.1 on 2022-11-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('motto', models.CharField(max_length=200)),
                ('logo', models.FileField(blank=True, null=True, upload_to='images/logo')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
