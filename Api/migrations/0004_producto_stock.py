# Generated by Django 5.1.5 on 2025-02-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_rename_direccion_cliente_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
