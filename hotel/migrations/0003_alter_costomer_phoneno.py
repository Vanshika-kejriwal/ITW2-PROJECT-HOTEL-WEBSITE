# Generated by Django 3.2.6 on 2021-09-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_costomer_id_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costomer',
            name='phoneNo',
            field=models.CharField(max_length=20),
        ),
    ]
