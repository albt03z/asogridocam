from django.urls import path
from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('aboutus/', AboutView.as_view(), name='about'),
    path('contactus/', ContactView.as_view(), name='contact'),
]