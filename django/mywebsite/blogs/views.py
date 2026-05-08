from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import BlogPostForm, UserProfileForm, UserUpdateForm
from .models import BlogPost, UserProfile


def home_page(request):
    latest_posts = BlogPost.objects.filter(is_approved=True)[:3]
    return render(
        request,
        "blogs/index.html",
        {
            "current_page": "Home",
            "latest_posts": latest_posts,
        },
    )


def blogposts(request):
    posts = BlogPost.objects.filter(is_approved=True)
    return render(
        request,
        "blogs/posts.html",
        {
            "current_page": "All Posts",
            "posts": posts,
            "total_posts": posts.count(),
        },
    )


def blog_post(request, blog):
    post = get_object_or_404(BlogPost, slug=blog, is_approved=True)
    return render(
        request,
        "blogs/post_detail.html",
        {
            "current_page": post.title,
            "parent_page": "All Posts",
            "parent_url": reverse("allpost"),
            "post": post,
        },
    )


@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.is_approved = False
            post.save()
            messages.success(request, "Your post was submitted and is waiting for admin approval.")
            return redirect("allpost")
    else:
        form = BlogPostForm()

    return render(
        request,
        "blogs/create_post.html",
        {
            "current_page": "Write Post",
            "parent_page": "All Posts",
            "parent_url": reverse("allpost"),
            "form": form,
        },
    )


@login_required
def dashboard(request):
    user_posts = BlogPost.objects.filter(author=request.user)
    approved_count = user_posts.filter(is_approved=True).count()
    pending_count = user_posts.filter(is_approved=False).count()
    total_posts = user_posts.count()
    total_words = sum(len(post.content.split()) for post in user_posts)
    approval_rate = round((approved_count / total_posts) * 100) if total_posts else 0
    average_words = round(total_words / total_posts) if total_posts else 0
    category_counts = list(
        user_posts.values("category__name")
        .annotate(total=Count("id"))
        .order_by("-total", "category__name")
    )
    top_category_total = max([item["total"] for item in category_counts], default=1)

    for category in category_counts:
        category["name"] = category["category__name"]
        category["percent"] = round((category["total"] / top_category_total) * 100)

    return render(
        request,
        "blogs/dashboard.html",
        {
            "current_page": "Dashboard",
            "stats": {
                "total_posts": total_posts,
                "approved_posts": approved_count,
                "pending_posts": pending_count,
                "public_posts": BlogPost.objects.filter(is_approved=True).count(),
                "approval_rate": approval_rate,
                "total_words": total_words,
                "average_words": average_words,
            },
            "category_counts": category_counts,
            "recent_posts": user_posts[:5],
        },
    )


@login_required
def profile(request):
    profile_obj, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_obj)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile was updated.")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile_obj)

    return render(
        request,
        "blogs/profile.html",
        {
            "current_page": "Profile",
            "user_form": user_form,
            "profile_form": profile_form,
            "profile": profile_obj,
        },
    )


def not_found(request, exception=None):
    return render(
        request,
        "404.html",
        {
            "current_page": "Page Not Found",
            "parent_page": "Home",
            "parent_url": reverse("home"),
        },
        status=404,
    )
