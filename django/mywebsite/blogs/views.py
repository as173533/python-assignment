from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
BLOG_POSTS = {
    "python-opps": {
        "title": "Python OOPs",
        "category": "Python",
        "reading_time": "4 min read",
        "summary": "Learn how classes, objects, inheritance, and encapsulation help structure Python code cleanly.",
        "content": [
            "Object-oriented programming in Python groups related data and behavior together.",
            "It becomes easier to reuse logic when classes represent clear real-world or business concepts.",
            "Start small, keep responsibilities narrow, and prefer readable methods over clever abstractions.",
        ],
    },
    "python-basics": {
        "title": "Python Basics",
        "category": "Python",
        "reading_time": "3 min read",
        "summary": "A quick path through variables, loops, conditions, and functions for building confidence early.",
        "content": [
            "Python basics are the foundation for every larger project you will build later.",
            "Focus first on syntax, conditions, loops, and functions before reaching for advanced topics.",
            "Small daily exercises are usually more effective than trying to learn everything in one session.",
        ],
    },
    "django-basics": {
        "title": "Django Basics",
        "category": "Django",
        "reading_time": "5 min read",
        "summary": "Understand URLs, views, templates, and how Django connects them into a working web app.",
        "content": [
            "Django follows a clear request-to-response flow using URL routing, views, and templates.",
            "Once you understand that flow, adding new pages becomes much easier and more predictable.",
            "Keep templates simple, keep views focused, and move repeated patterns into reusable components.",
        ],
    },
    "regex": {
        "title": "Regex in Practice",
        "category": "Utilities",
        "reading_time": "4 min read",
        "summary": "Use regular expressions to search, validate, and transform text without writing repetitive code.",
        "content": [
            "Regular expressions are useful when your input follows a pattern and simple string methods are not enough.",
            "Good regex patterns are precise, tested, and documented so they remain maintainable later.",
            "Use regex carefully and favor clarity over compact patterns that are difficult to debug.",
        ],
    },
}


def build_blog_listing():
    posts = []
    for slug, post in BLOG_POSTS.items():
        posts.append(
            {
                "slug": slug,
                "url": reverse("blog-post", args=[slug]),
                **post,
            }
        )
    return posts


def home_page(request):
    return render(request, "blogs/index.html")


def blogposts(request):
    return render(
        request,
        "blogs/posts.html",
        {
            "posts": build_blog_listing(),
            "total_posts": len(BLOG_POSTS),
        },
    )


# def python_intro(request):
#     return HttpResponse("Python Introduction Post")
#
# def django_basics(request):
#     return HttpResponse("Django Basics Blog Post")


def blog_post(request, blog):
    post = BLOG_POSTS.get(blog)
    if post is None:
        raise Http404(f"No blog post found for '{blog}'.")

    return render(
        request,
        "blogs/post_detail.html",
        {
            "post": {
                "slug": blog,
                "back_url": reverse("allpost"),
                **post,
            }
        },
    )

