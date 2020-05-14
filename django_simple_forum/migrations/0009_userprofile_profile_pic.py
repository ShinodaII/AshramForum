from __future__ import unicode_literals

from django.db import migrations, models
import django_simple_forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0008_auto_20160707_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to=django_simple_forum.models.img_url),
        ),
    ]
