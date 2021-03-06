from django.db import migrations, models
import django_simple_forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0014_auto_20170208_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=django_simple_forum.models.img_url),
        ),
    ]
