# Generated by Django 4.2.6 on 2023-10-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sebodediscos_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sebodediscos',
            name='ano',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sebodediscos',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]