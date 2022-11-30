# Generated by Django 4.1.2 on 2022-11-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
