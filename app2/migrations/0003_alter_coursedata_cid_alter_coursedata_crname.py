# Generated by Django 5.1 on 2024-08-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_coursedata_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedata',
            name='cid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coursedata',
            name='crname',
            field=models.CharField(max_length=100),
        ),
    ]
