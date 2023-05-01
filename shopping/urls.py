from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .yasg import urlpatterns as doc_urls


schema_view = get_schema_view(
    openapi.Info(
        title='Market',
        default_version='v1',
        description='shop',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='asbfaseyfy@gmail.com'),
        license=openapi.License(name='Test-lisense'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/api/', include('rest_framework.urls')),
    path('admin-panel/', admin.site.urls),

    path('', include(('accounts.urls', "accounts"), namespace="account")),
    path('', include('address.urls')),
    path('', include('product.urls')),
    path('', include('category.urls')),
    path('', include('cart.urls')),
    path('', include('order.urls')),
    path('', include('service.content_type.urls')),
    # path('', include(('accounts.urls', "accounts"), namespace="account")),
    # path('', include('refactoring.products.product.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
 ]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
