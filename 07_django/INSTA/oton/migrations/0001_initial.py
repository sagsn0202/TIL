# Generated by Django 2.1.7 on 2019-04-15 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oton.Writer'),
        ),
    ]