# Generated by Django 4.2.1 on 2024-07-11 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(editable=False, max_length=6, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('roll_no', models.CharField(max_length=50, unique=True)),
                ('student_class', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=255)),
                ('parents_name', models.CharField(max_length=255)),
                ('parents_phone_number', models.CharField(max_length=15)),
                ('student_phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('interests', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='student_photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]