# Generated by Django 2.1.4 on 2018-12-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('first_number', models.IntegerField()),
                ('second_number', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
