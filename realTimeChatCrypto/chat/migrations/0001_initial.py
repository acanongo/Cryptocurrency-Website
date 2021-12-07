# Generated by Django 3.2.9 on 2021-11-04 17:51

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
            name='SuggestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestionText', models.CharField(max_length=400)),
                ('datePublished', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(max_length=200, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('imageDescription', models.CharField(max_length=240, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.CharField(max_length=400)),
                ('datePublished', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.suggestionmodel')),
            ],
        ),
    ]
