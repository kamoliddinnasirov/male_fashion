from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += i18n_patterns(
    path("shop/", include("shop.urls")),
    path("blog/", include("blog.urls")),
    path("", include("pages.urls")),
    path("users/", include("users.urls")),
    path("orders/", include('orders.urls'))
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
