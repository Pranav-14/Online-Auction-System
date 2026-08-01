from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listing, Bid, Comment, Category, OTPVerification


def index(request):
    if request.user.is_authenticated:
        request.session["number_watchlist"] = (
            User.objects.get(username=request.user.username).watchlist.all().count()
        )

    return render(
        request,
        "auctions/index.html",
        {"listings": Listing.objects.all().reverse(), "title": "Active Listings"},
    )


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def request_otp_view(request):
    """View to enter an Indian mobile (+91) number and send 6-digit OTP"""
    if request.method == "POST":
        raw_phone = request.POST.get("phone_number", "").strip()
        digits = "".join(filter(str.isdigit, raw_phone))

        if len(digits) == 10:
            formatted_phone = f"+91{digits}"
        elif len(digits) == 12 and digits.startswith("91"):
            formatted_phone = f"+{digits}"
        else:
            return render(
                request,
                "auctions/otp_request.html",
                {"message": "Please enter a valid 10-digit Indian mobile number."},
            )

        otp_obj = OTPVerification.generate_otp(formatted_phone)
        request.session["otp_phone_number"] = formatted_phone

        # Log OTP code to server output for local testing & development
        print(f"\n==========================================", flush=True)
        print(
            f"[OTP SERVICE] Sent OTP: {otp_obj.otp_code} to {formatted_phone}",
            flush=True,
        )
        print(f"==========================================\n", flush=True)

        return HttpResponseRedirect(reverse("verify_otp"))

    return render(request, "auctions/otp_request.html")


def verify_otp_view(request):
    """View to enter 6-digit OTP code and authenticate user"""
    phone_number = request.session.get("otp_phone_number")
    if not phone_number:
        return HttpResponseRedirect(reverse("request_otp"))

    if request.method == "POST":
        entered_code = request.POST.get("otp_code", "").strip()
        otp_obj = OTPVerification.objects.filter(
            phone_number=phone_number, is_used=False
        ).first()

        if otp_obj and otp_obj.is_valid() and otp_obj.otp_code == entered_code:
            otp_obj.is_used = True
            otp_obj.save()

            # Find or auto-create User for verified Indian mobile number
            user = User.objects.filter(phone_number=phone_number).first()
            if not user:
                clean_username = f"user_{phone_number[-10:]}"
                user = User.objects.create_user(
                    username=clean_username,
                    phone_number=phone_number,
                    is_phone_verified=True,
                )
            else:
                user.is_phone_verified = True
                user.save()

            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/otp_verify.html",
                {
                    "phone_number": phone_number,
                    "message": "Invalid or expired OTP code. Please try again.",
                },
            )

    return render(request, "auctions/otp_verify.html", {"phone_number": phone_number})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        phone_number = request.POST.get("phone_number", "").strip()

        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        try:
            user = User.objects.create_user(username, email, password)
            if phone_number:
                user.phone_number = phone_number
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username or phone number already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


class NewListingForm(forms.Form):
    title = forms.CharField(label="Title", max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    bid = forms.FloatField(label="Current Bid", min_value=0.0)
    url = forms.URLField(label="Image URL")
    category = forms.ModelChoiceField(queryset=Category.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()


@login_required
def create(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            bid = form.cleaned_data["bid"]
            url = form.cleaned_data["url"]
            category = form.cleaned_data["category"]
            new = Listing(
                title=title,
                description=description,
                current_bid=bid,
                image_url=url,
                category=category,
                user=request.user,
            )
            new.save()
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(
            request,
            "auctions/create.html",
            {
                "form": NewListingForm(),
            },
        )


def listing(request, listing_id):
    lstng = Listing.objects.get(id=listing_id)
    watchlisted = False

    if request.user.is_authenticated:
        for users in lstng.watchlist_users.all():
            if users == request.user:
                watchlisted = True
                break

    number_of_bids = lstng.bids.all().count()

    if request.method == "POST":
        new_bid = int(request.POST["new_bid"])

        if new_bid <= lstng.current_bid:
            return render(
                request,
                "auctions/listing.html",
                {
                    "listing": lstng,
                    "watchlisted": watchlisted,
                    "number_of_bids": number_of_bids,
                    "error_bid": "Your bid must be greater than the current bid.",
                },
            )
        else:
            lstng.current_bid = new_bid
            lstng.save()

            lstng2 = Listing.objects.get(id=listing_id)
            bid = Bid(bidder=request.user, amount=new_bid, listing=lstng2)
            bid.save()

            number_of_bids2 = lstng2.bids.all().count()

            return render(
                request,
                "auctions/listing.html",
                {
                    "listing": lstng2,
                    "watchlisted": watchlisted,
                    "number_of_bids": number_of_bids2,
                    "success_bid": "Your bid has been placed.",
                },
            )

    else:
        return render(
            request,
            "auctions/listing.html",
            {
                "listing": lstng,
                "watchlisted": watchlisted,
                "number_of_bids": number_of_bids,
            },
        )


@login_required
def comment(request, listing_id):
    if request.method == "POST":
        new_comment = Comment(
            user=request.user,
            comment=request.POST["newcomment"],
            listing=Listing.objects.get(id=listing_id),
        )
        new_comment.save()
        return HttpResponseRedirect(
            reverse("listing", kwargs={"listing_id": listing_id})
        )


@login_required
def my_watchlist(request):
    return render(
        request,
        "auctions/index.html",
        {
            "listings": User.objects.get(
                username=request.user.username
            ).watchlist.all(),
            "title": "My Watchlist",
        },
    )


@login_required
def watchlist(request, listing_id=0):
    if request.method == "POST" and request.POST.get("addwatchlist", False):
        lst = Listing.objects.get(id=listing_id)
        lst.watchlist_users.add(request.user)
        request.session["number_watchlist"] = (
            User.objects.get(username=request.user.username).watchlist.all().count()
        )
        return HttpResponseRedirect(
            reverse("listing", kwargs={"listing_id": listing_id})
        )

    elif request.method == "POST" and request.POST.get("removewatchlist", False):
        lst = Listing.objects.get(id=listing_id)
        lst.watchlist_users.remove(request.user)
        request.session["number_watchlist"] = (
            User.objects.get(username=request.user.username).watchlist.all().count()
        )
        return HttpResponseRedirect(
            reverse("listing", kwargs={"listing_id": listing_id})
        )


def categories(request):
    return render(
        request,
        "auctions/categories.html",
        {
            "categories": Category.objects.all(),
        },
    )


def category(request, name):
    listings = Category.objects.get(category=name.title()).all_listings.all()
    return render(
        request,
        "auctions/index.html",
        {"listings": listings, "title": f"All listings in {name.title()} category"},
    )


def close_auction(request, idd):
    lst = Listing.objects.get(id=idd)
    lst.is_active = False
    lst.save()

    return HttpResponseRedirect(reverse("index"))
