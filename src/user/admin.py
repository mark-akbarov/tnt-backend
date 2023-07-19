from django.contrib import admin
from user.models.base import User
from user.models.otp_verification import OTPVerification


admin.site.register(User)
admin.site.register(OTPVerification)