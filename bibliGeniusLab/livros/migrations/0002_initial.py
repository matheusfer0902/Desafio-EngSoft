# Generated by Django 5.1.2 on 2024-11-05 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=255)),
                ('editora', models.CharField(default=1)),
                ('data_publicacao', models.DateField()),
                ('genero', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
    ]
