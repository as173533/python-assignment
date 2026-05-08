from django.contrib import admin

from .models import BlogPost, Category, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "is_approved", "created_at")
    list_filter = ("is_approved", "category", "created_at")
    search_fields = ("title", "summary", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    actions = ["approve_posts"]

    @admin.action(description="Approve selected posts")
    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")
    search_fields = ("user__username", "user__email", "bio")
