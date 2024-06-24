# Generated by Django 5.0.6 on 2024-06-21 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Endereco",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rua", models.CharField(max_length=100)),
                ("numero", models.IntegerField()),
                ("bairro", models.CharField(max_length=100)),
                ("cidade", models.CharField(max_length=100)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranão"),
                            ("MG", "Minas Gerais"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MT", "Mato Grosso"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PE", "Pernanbuco"),
                            ("PI", "Piauí"),
                            ("PR", "Paraná"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("RS", "Rio Grande do Sul"),
                            ("SC", "Santa Catarina"),
                            ("SE", "Sergipe"),
                            ("SP", "São Paulo"),
                            ("TO", "Tocantins"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Atendente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "clientes",
                    models.ManyToManyField(
                        related_name="atendente_cliente", to="clientes.cliente"
                    ),
                ),
            ],
            options={
                "db_table": "app_funcionario",
            },
        ),
        migrations.CreateModel(
            name="Dependente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=12)),
                (
                    "titular",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dependente",
                        to="clientes.cliente",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cliente",
            name="endereco",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clientes.endereco",
            ),
        ),
    ]