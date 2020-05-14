from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_simple_forum.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_simple_forum', '0004_topic_no_of_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('attached_file', models.FileField(blank=True, max_length=500, null=True, upload_to=django_simple_forum.models.img_url)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_simple_forum.Comment')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
