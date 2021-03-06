# Generated by Django 3.0.6 on 2020-05-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('learn_list1', models.CharField(max_length=250)),
                ('learn_list2', models.CharField(max_length=250)),
                ('learn_list3', models.CharField(blank=True, max_length=250)),
                ('completion_list1', models.CharField(max_length=250)),
                ('completion_list2', models.CharField(blank=True, max_length=250)),
                ('category', models.CharField(max_length=50)),
                ('weekday_datetime', models.DateField()),
                ('weekends_datetime', models.DateField()),
                ('photo_course', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_next_event', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
