# Generated by Django 2.0.8 on 2018-09-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
