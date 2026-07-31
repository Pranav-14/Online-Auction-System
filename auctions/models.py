import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="Indian Mobile Number starting with +91 or 10-digit number",
    )
    is_phone_verified = models.BooleanField(default=False)

    def clean_phone_number(self):
        """Helper to standardize Indian mobile numbers into +91 format"""
        if not self.phone_number:
            return None
        digits = "".join(filter(str.isdigit, str(self.phone_number)))
        if len(digits) == 10:
            return f"+91{digits}"
        elif len(digits) == 12 and digits.startswith("91"):
            return f"+{digits}"
        return self.phone_number


class OTPVerification(models.Model):
    phone_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    @classmethod
    def generate_otp(cls, phone_number):
        """Invalidate older unused OTPs and create a fresh 6-digit OTP code"""
        cls.objects.filter(phone_number=phone_number, is_used=False).update(
            is_used=True
        )
        code = f"{random.randint(100000, 999999)}"
        return cls.objects.create(phone_number=phone_number, otp_code=code)

    def is_valid(self):
        """OTP is valid for 10 minutes (600 seconds) if unused"""
        if self.is_used:
            return False
        elapsed = (timezone.now() - self.created_at).total_seconds()
        return elapsed < 600

    def __str__(self):
        return f"OTP for {self.phone_number}: {self.otp_code}"


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
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="all_listings"
    )
    created = models.DateTimeField(auto_now_add=True)
    watchlist_users = models.ManyToManyField(User, related_name="watchlist", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}: ₹{self.current_bid} by {self.user.username}"


class Bid(models.Model):
    bidder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bids_placed"
    )
    amount = models.FloatField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.bidder}: ₹{self.amount} on {self.listing.title}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_user"
    )
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.DO_NOTHING, related_name="comments"
    )

    def __str__(self):
        return f"{self.user}: {self.listing.title}"
