from django.db import migrations
from django.utils.text import slugify


DEFAULT_CATEGORIES = [
    "Django",
    "Python",
    "Web Development",
    "Utilities",
    "Tutorials",
]


def unique_slug(Category, name):
    base_slug = slugify(name) or "category"
    slug = base_slug
    counter = 2
    while Category.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


def migrate_categories(apps, schema_editor):
    Category = apps.get_model("blogs", "Category")
    BlogPost = apps.get_model("blogs", "BlogPost")

    for name in DEFAULT_CATEGORIES:
        Category.objects.get_or_create(
            name=name,
            defaults={"slug": unique_slug(Category, name)},
        )

    for post in BlogPost.objects.all():
        name = (post.category or "Uncategorized").strip() or "Uncategorized"
        category, _ = Category.objects.get_or_create(
            name=name,
            defaults={"slug": unique_slug(Category, name)},
        )
        post.category_ref = category
        post.save(update_fields=["category_ref"])


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_category_and_post_category_ref"),
    ]

    operations = [
        migrations.RunPython(migrate_categories, migrations.RunPython.noop),
    ]
