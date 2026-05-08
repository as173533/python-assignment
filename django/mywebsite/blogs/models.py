from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.FileField(upload_to="profile-images/", blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return f"https://placehold.co/160x160?text={self.user.username[:1].upper()}"


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 2
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",
    )
    summary = models.CharField(max_length=280)
    content = models.TextField()
    image = models.FileField(upload_to="blog-images/", blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 2
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog-post", args=[self.slug])

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://placehold.co/900x520?text=Blog+Image"

    @property
    def reading_time(self):
        words = len(self.content.split())
        minutes = max(1, round(words / 200))
        return f"{minutes} min read"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
