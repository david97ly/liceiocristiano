# Generated by Django 2.0.5 on 2019-04-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liceo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='comentario',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='institucion_actual',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='telefono',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
