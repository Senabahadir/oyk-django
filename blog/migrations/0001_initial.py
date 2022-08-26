# Generated by Django 4.1 on 2022-08-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yayinla', models.BooleanField(default=False)),
                ('baslik', models.CharField(max_length=200, unique=True)),
                ('link', models.SlugField(max_length=200, unique=True)),
                ('resim', models.ImageField(upload_to='blog_resim/')),
                ('icerik', models.TextField()),
            ],
        ),
    ]
