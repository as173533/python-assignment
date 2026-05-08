import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0005_migrate_post_categories"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="category",
        ),
        migrations.RenameField(
            model_name="blogpost",
            old_name="category_ref",
            new_name="category",
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="posts",
                to="blogs.category",
            ),
        ),
    ]
