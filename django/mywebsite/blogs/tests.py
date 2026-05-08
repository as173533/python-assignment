from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import BlogPost, Category


class BlogPageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="writer",
            password="testpass123",
        )
        self.category, _ = Category.objects.get_or_create(
            name="Utilities",
            defaults={"slug": "utilities"},
        )
        self.post = BlogPost.objects.create(
            title="Regex in Practice",
            author=self.user,
            category=self.category,
            summary="Use regular expressions to search and validate text.",
            content="Regular expressions are useful when your input follows a pattern.",
            is_approved=True,
        )

    def test_all_posts_page_renders_approved_cards(self):
        response = self.client.get(reverse("allpost"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/posts.html")
        self.assertContains(response, "Explore every post in one place.")
        self.assertContains(response, "Regex in Practice")
        self.assertContains(response, reverse("blog-post", args=[self.post.slug]))

    def test_single_post_page_renders_requested_post(self):
        response = self.client.get(reverse("blog-post", args=[self.post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/post_detail.html")
        self.assertContains(response, "Regex in Practice")
        self.assertContains(response, "Regular expressions are useful")

    def test_unapproved_post_does_not_render_publicly(self):
        pending_post = BlogPost.objects.create(
            title="Waiting for Review",
            author=self.user,
            category=self.category,
            summary="This should not be visible yet.",
            content="Admin needs to approve this post first.",
            is_approved=False,
        )

        listing_response = self.client.get(reverse("allpost"))
        detail_response = self.client.get(reverse("blog-post", args=[pending_post.slug]))

        self.assertNotContains(listing_response, "Waiting for Review")
        self.assertEqual(detail_response.status_code, 404)

    def test_create_post_requires_login(self):
        response = self.client.get(reverse("create-post"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    def test_create_post_shows_required_field_errors(self):
        self.client.login(username="writer", password="testpass123")

        response = self.client.post(reverse("create-post"), data={})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "has-error")

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    def test_logged_in_user_can_view_dashboard_and_profile(self):
        self.client.login(username="writer", password="testpass123")

        dashboard_response = self.client.get(reverse("dashboard"))
        profile_response = self.client.get(reverse("profile"))

        self.assertEqual(dashboard_response.status_code, 200)
        self.assertContains(dashboard_response, "Writer Dashboard")
        self.assertContains(dashboard_response, "Category Analytics")
        self.assertContains(dashboard_response, "Approval Rate")
        self.assertEqual(profile_response.status_code, 200)
        self.assertContains(profile_response, "Edit profile.")

    def test_logged_in_header_shows_account_menu_not_login_link(self):
        self.client.login(username="writer", password="testpass123")

        response = self.client.get(reverse("allpost"))

        self.assertContains(response, "Dashboard")
        self.assertContains(response, "Profile")
        self.assertNotContains(response, ">Login</a>")
