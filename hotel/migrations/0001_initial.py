# Generated by Django 3.2.6 on 2021-08-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='costomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('IDproof', models.CharField(max_length=100)),
                ('ID_num', models.IntegerField()),
                ('phoneNo', models.IntegerField()),
                ('males', models.IntegerField()),
                ('females', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
        ),
    ]
