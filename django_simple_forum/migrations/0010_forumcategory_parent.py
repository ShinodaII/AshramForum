from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0009_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_simple_forum.ForumCategory'),
        ),
    ]
