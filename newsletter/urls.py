from django.urls import path
from .views import newsletter_signup, newsletter_success

urlpatterns = [
    path('signup/', newsletter_signup, name='newsletter_signup'),
    path('success/', newsletter_success, name='newsletter_success'),
]