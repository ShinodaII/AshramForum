from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_by', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_parent', to='django_simple_forum.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='ForumCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
                ('color', models.CharField(default='#999999', max_length=20)),
                ('is_votable', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('namespace', models.CharField(db_index=True, default='default', max_length=250)),
                ('event_type', models.CharField(db_index=True, max_length=250)),
                ('data', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type_timelines', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Disabled', 'Disabled')], max_length=10)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('no_of_views', models.IntegerField(default='0')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_simple_forum.ForumCategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_votes', models.IntegerField(default='0')),
                ('user_roles', models.CharField(choices=[('Admin', 'Admin'), ('Publisher', 'Publisher')], max_length=10)),
                ('badges', models.ManyToManyField(to='django_simple_forum.Badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_followed', models.BooleanField(default=False)),
                ('followed_on', models.DateField(blank=True, null=True)),
                ('no_of_votes', models.IntegerField(default='0')),
                ('is_like', models.BooleanField(default=False)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_simple_forum.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_comments', to='django_simple_forum.Topic'),
        ),
        migrations.AlterIndexTogether(
            name='timeline',
            index_together=set([('content_type', 'object_id', 'namespace')]),
        ),
    ]
