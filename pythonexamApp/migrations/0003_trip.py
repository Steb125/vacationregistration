# Generated by Django 2.2.4 on 2020-10-21 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pythonexamApp', '0002_auto_20201020_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joiner', models.ManyToManyField(related_name='trip_joined', to='pythonexamApp.User')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_added', to='pythonexamApp.User')),
            ],
        ),
    ]