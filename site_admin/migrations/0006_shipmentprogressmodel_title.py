# Generated by Django 4.1.1 on 2022-11-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0005_alter_shipmentprogressmodel_shipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentprogressmodel',
            name='title',
            field=models.CharField(default='h', max_length=200),
            preserve_default=False,
        ),
    ]
