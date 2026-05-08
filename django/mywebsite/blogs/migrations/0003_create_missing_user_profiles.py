from django.conf import settings
from django.db import migrations


def create_missing_profiles(apps, schema_editor):
    user_model_name = settings.AUTH_USER_MODEL.split(".")
    User = apps.get_model(user_model_name[0], user_model_name[1])
    UserProfile = apps.get_model("blogs", "UserProfile")

    for user in User.objects.all():
        UserProfile.objects.get_or_create(user=user)


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_userprofile"),
    ]

    operations = [
        migrations.RunPython(create_missing_profiles, migrations.RunPython.noop),
    ]
