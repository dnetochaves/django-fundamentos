# Generated by Django 5.0.6 on 2024-06-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0003_cliente_nivel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="profissao",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
