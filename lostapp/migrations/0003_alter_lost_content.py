# Generated by Django 4.1.2 on 2022-10-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostapp', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='content',
            field=models.TextField(max_length=400),
        ),
    ]