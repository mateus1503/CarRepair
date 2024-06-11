# Generated by Django 5.0.6 on 2024-06-11 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_alter_pessoa_sexo'),
        ('empresas', '0001_initial'),
        ('veiculo', '0004_delete_fabricante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='veiculo.veiculo')),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa')),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
    ]
