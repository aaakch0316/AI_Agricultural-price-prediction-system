# Generated by Django 3.1.7 on 2021-04-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_mainprice_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_1', models.TextField()),
                ('o_2', models.TextField()),
                ('o_3', models.TextField()),
                ('o_4', models.TextField()),
                ('o_5', models.TextField()),
                ('o_6', models.TextField()),
                ('o_7', models.TextField()),
                ('o_8', models.TextField()),
                ('o_9', models.TextField()),
                ('o_10', models.TextField()),
                ('o_11', models.TextField()),
                ('o_12', models.TextField()),
                ('o_13', models.TextField()),
                ('o_14', models.TextField()),
                ('o_15', models.TextField()),
                ('o_16', models.TextField()),
                ('o_17', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PredictPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('b_7', models.TextField()),
                ('b_6', models.TextField()),
                ('b_5', models.TextField()),
                ('b_4', models.TextField()),
                ('b_3', models.TextField()),
                ('b_2', models.TextField()),
                ('b_1', models.TextField()),
                ('b_0', models.TextField()),
                ('a_1', models.TextField()),
                ('a_2', models.TextField()),
                ('a_3', models.TextField()),
                ('a_4', models.TextField()),
                ('a_5', models.TextField()),
                ('a_6', models.TextField()),
                ('a_7', models.TextField()),
            ],
        ),
    ]