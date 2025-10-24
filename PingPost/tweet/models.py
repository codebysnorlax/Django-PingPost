from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

# Model for user posts (tweets)
class Tweet(models.Model):
    # Connected user; delete tweets if user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Post text (max 250 chars)
    text = models.TextField(max_length=250)

    # Optional image upload (stored in photos/)
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        null=True
    )

    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # When created
    updated_at = models.DateTimeField(auto_now=True)      # When updated

    # Delete image file when tweet is removed
    def delete(self, *args, **kwargs):
        if self.photo and os.path.isfile(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    # Display username and short text in admin/debug
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
