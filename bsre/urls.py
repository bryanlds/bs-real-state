from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("src.apps.pages.urls")),
    path("listings/", include("src.apps.listings.urls")),
    path("accounts/", include("src.apps.accounts.urls")),
    path("contacts/", include("src.apps.contacts.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
