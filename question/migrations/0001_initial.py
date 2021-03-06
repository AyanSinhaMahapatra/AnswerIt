# Generated by Django 2.0.5 on 2018-05-09 08:03

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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=10000)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('dislike_users', models.ManyToManyField(blank=True, related_name='downvote_ans', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(blank=True, related_name='upvote_ans', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ans_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=10000)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_ans', to='question.Answer')),
                ('dislike_users', models.ManyToManyField(blank=True, related_name='downvote_com', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(blank=True, related_name='upvote_com', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=10000)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(max_length=1000)),
                ('dislike_users', models.ManyToManyField(blank=True, related_name='downvote_ques', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(blank=True, related_name='upvote_ques', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ques_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(blank=True, to='question.Tag'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_ques', to='question.Question'),
        ),
    ]
