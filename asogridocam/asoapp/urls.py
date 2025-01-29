from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('aboutus/', AboutView.as_view(), name='about'),
    path('contactus/', ContactView.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)