# Generated by Django 2.0.6 on 2018-06-21 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('startdate', models.TimeField()),
                ('enddate', models.TimeField()),
                ('difficulty', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
                ('incorrect_answers', models.CharField(max_length=255)),
                ('game', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quiz.Game')),
            ],
        ),
    ]
