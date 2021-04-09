# Generated by Django 3.1.7 on 2021-04-07 17:06

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('answer_text', tinymce.models.HTMLField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
            ],
        ),
    ]
