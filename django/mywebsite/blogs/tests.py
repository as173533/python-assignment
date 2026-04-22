from django.test import TestCase
from django.urls import reverse


class BlogPageTests(TestCase):
    def test_all_posts_page_renders_dynamic_cards(self):
        response = self.client.get(reverse("allpost"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/posts.html")
        self.assertContains(response, "Explore every post in one place.")
        self.assertContains(response, "Python OOPs")
        self.assertContains(response, reverse("blog-post", args=["python-opps"]))

    def test_single_post_page_renders_requested_post(self):
        response = self.client.get(reverse("blog-post", args=["regex"]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/post_detail.html")
        self.assertContains(response, "Regex in Practice")
        self.assertContains(response, "Regular expressions are useful")

    def test_missing_post_returns_404(self):
        response = self.client.get(reverse("blog-post", args=["missing-post"]))

        self.assertEqual(response.status_code, 404)
