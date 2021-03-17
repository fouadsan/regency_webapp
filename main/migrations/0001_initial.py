# Generated by Django 3.1.7 on 2021-03-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('since', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Mining', 'Mining'), ('Agriculture', 'Agriculture'), ('Infrastructure', 'Infrastructure'), ('Power', 'Power')], default='Mining', max_length=20, unique=True)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('description', models.CharField(default='this is a description about this service', max_length=250)),
                ('image_one', models.ImageField(upload_to='images')),
                ('image_two', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('occupation', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('testimonial', models.TextField()),
                ('occupation', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image_one', models.ImageField(upload_to='images')),
                ('image_two', models.ImageField(blank=True, upload_to='images')),
                ('image_three', models.ImageField(blank=True, upload_to='images')),
                ('image_four', models.ImageField(blank=True, upload_to='images')),
                ('project_url', models.URLField(blank=True, unique=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='main.section')),
            ],
        ),
    ]
