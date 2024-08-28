import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    current_bid = models.FloatField()
    image_url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='all_listings')
    created = models.DateTimeField(auto_now_add=True)
    watchlist_users = models.ManyToManyField(User, related_name='watchlist', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}: ${self.current_bid} by {self.user.username}"


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_placed")
    amount = models.FloatField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.bidder}: ${self.amount} on {self.listing.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING, related_name="comments")

    def __str__(self):
        return f"{self.user}: {self.listing.title}"


