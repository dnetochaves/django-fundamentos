# Generated by Django 5.0.6 on 2024-06-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0002_endereco_atendente_dependente_cliente_endereco"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="nivel",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
