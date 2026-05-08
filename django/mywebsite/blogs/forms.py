from django import forms
from django.contrib.auth import get_user_model

from .models import BlogPost, Category, UserProfile


class BlogPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        error_messages={"required": "This field is required."},
    )

    class Meta:
        model = BlogPost
        fields = ["title", "category", "summary", "content", "image"]
        error_messages = {
            "title": {"required": "This field is required."},
            "summary": {"required": "This field is required."},
            "content": {"required": "This field is required."},
        }
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3}),
            "content": forms.Textarea(attrs={"rows": 10}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters.")
        return title

    def clean_summary(self):
        summary = self.cleaned_data["summary"].strip()
        if len(summary) < 20:
            raise forms.ValidationError("Summary must be at least 20 characters.")
        return summary

    def clean_content(self):
        content = self.cleaned_data["content"].strip()
        if len(content.split()) < 10:
            raise forms.ValidationError("Content must contain at least 10 words.")
        return content

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image

        content_type = getattr(image, "content_type", "")
        if not content_type.startswith("image/"):
            raise forms.ValidationError("Please upload a valid image file.")

        if image.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Image size must be 2 MB or less.")

        return image


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
        error_messages = {
            "email": {"invalid": "Enter a valid email address."},
        }

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar", "bio"]

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if not avatar:
            return avatar

        content_type = getattr(avatar, "content_type", "")
        if not content_type.startswith("image/"):
            raise forms.ValidationError("Please upload a valid image file.")

        if avatar.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Avatar size must be 2 MB or less.")

        return avatar
