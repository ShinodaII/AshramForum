from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0005_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumcategory',
            name='description',
            field=models.TextField(default=datetime.datetime(2016, 7, 7, 6, 27, 51, 32010)),
            preserve_default=False,
        ),
    ]
