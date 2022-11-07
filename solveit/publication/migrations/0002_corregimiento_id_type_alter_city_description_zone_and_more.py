# Generated by Django 4.1.3 on 2022-11-07 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corregimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Id_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('corregimiento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.corregimiento', verbose_name='Corregimiento')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Lastname')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('idnumber', models.PositiveIntegerField(verbose_name='Id_Number')),
                ('phone', models.PositiveIntegerField(default=0, verbose_name='Phone')),
                ('mail', models.EmailField(max_length=254, verbose_name='Mail')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('idType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.id_type', verbose_name='Id_Type')),
                ('zone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.zone', verbose_name='Zone')),
            ],
        ),
        migrations.AddField(
            model_name='corregimiento',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.city', verbose_name='City'),
        ),
    ]
