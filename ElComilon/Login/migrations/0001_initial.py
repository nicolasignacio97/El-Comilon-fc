# Generated by Django 3.2.7 on 2021-10-25 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rutcliente', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombreusuario', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=30)),
                ('saldocli', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpresaConvenio',
            fields=[
                ('rutempresaconvenio', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('razonsocial', models.CharField(max_length=30)),
                ('fechaconvenio', models.DateField()),
            ],
            options={
                'db_table': 'empresa_convenio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('idtipocliente', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipo_cliente',
                'managed': False,
            },
        ),
    ]
