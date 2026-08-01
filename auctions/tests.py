from django.test import TestCase, Client
from django.urls import reverse
from auctions.models import User, OTPVerification


class IndianAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_phone = "+919876543210"

    def test_user_indian_phone_cleaning(self):
        """Test formatting of 10-digit Indian phone numbers into +91 standard format"""
        user = User(username="testuser", phone_number="9876543210")
        self.assertEqual(user.clean_phone_number(), "+919876543210")

    def test_otp_generation_and_validation(self):
        """Test OTP generation, validation, and single-use state"""
        otp = OTPVerification.generate_otp(self.test_phone)
        self.assertEqual(len(otp.otp_code), 6)
        self.assertTrue(otp.is_valid())

        # Test marking OTP as used
        otp.is_used = True
        otp.save()
        self.assertFalse(otp.is_valid())

    def test_request_otp_view(self):
        """Test requesting OTP code for a valid 10-digit mobile number"""
        response = self.client.post(
            reverse("request_otp"), {"phone_number": "9876543210"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get("otp_phone_number"), "+919876543210")
        self.assertEqual(
            OTPVerification.objects.filter(phone_number="+919876543210").count(), 1
        )

    def test_verify_otp_view_success(self):
        """Test verifying valid OTP code logs the user in and verifies phone number"""
        otp = OTPVerification.generate_otp(self.test_phone)

        # Set session phone
        session = self.client.session
        session["otp_phone_number"] = self.test_phone
        session.save()

        response = self.client.post(reverse("verify_otp"), {"otp_code": otp.otp_code})
        self.assertEqual(response.status_code, 302)

        # Check user created and verified
        user = User.objects.get(phone_number=self.test_phone)
        self.assertTrue(user.is_phone_verified)
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)
