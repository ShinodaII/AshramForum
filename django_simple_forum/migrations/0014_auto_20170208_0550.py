from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_simple_forum', '0013_userprofile_send_mailnotifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('U', 'Up'), ('D', 'Down')], max_length=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='topic',
            name='no_of_down_votes',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='no_of_votes',
        ),
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.ManyToManyField(to='django_simple_forum.Vote'),
        ),
        migrations.AddField(
            model_name='topic',
            name='votes',
            field=models.ManyToManyField(to='django_simple_forum.Vote'),
        ),
    ]
