from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0016_auto_20200329_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attached_file',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to='forum_topic/attachments/'),
        ),
    ]
