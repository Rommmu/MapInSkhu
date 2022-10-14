# Generated by Django 4.1.2 on 2022-10-14 11:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwan_num', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(13)])),
                ('kwan_name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('feedback_date', models.DateTimeField(auto_now_add=True)),
                ('user_phonenum', models.CharField(max_length=100, null=True)),
                ('feedback_content', models.TextField(default='글을 작성해주세요.')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('date1', models.CharField(max_length=10)),
                ('date2', models.CharField(max_length=10, null=True)),
                ('time1', models.TimeField()),
                ('time2', models.TimeField()),
                ('prof_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_profid', to='getherapp.professor')),
                ('room_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_roomid', to='getherapp.classroom')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_subid', to='getherapp.subject')),
            ],
        ),
    ]
