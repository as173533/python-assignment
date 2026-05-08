import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_create_missing_user_profiles"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                "ordering": ["name"],
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.AddField(
            model_name="blogpost",
            name="category_ref",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="posts_pending_migration",
                to="blogs.category",
            ),
        ),
    ]
