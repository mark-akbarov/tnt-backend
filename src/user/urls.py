from django.urls import path

from user.views.otp import OTPSignupView, OTPVerificationAPIView
from user.views.signup import SignupAPIView
from user.views.login import LoginAPIView
from user.views.verification import VerifyUserAPIView, ReSendVerifyUserAPIView


urlpatterns = [    
    path('otp/', OTPSignupView.as_view(), name='otp_signup'),
    path('otp/verify/', OTPVerificationAPIView.as_view(), name='otp_verification'),
    path('signup/', SignupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('verify/', VerifyUserAPIView.as_view()),
    path('verify/resend/', ReSendVerifyUserAPIView.as_view()),
]
