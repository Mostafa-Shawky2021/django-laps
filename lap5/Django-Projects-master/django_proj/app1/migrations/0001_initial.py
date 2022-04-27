# Generated by Django 4.0.4 on 2022-04-22 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(default='noname', max_length=20)),
                ('age', models.IntegerField()),
                ('student_track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.track')),
            ],
        ),
    ]
