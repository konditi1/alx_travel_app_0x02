from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from listings import views  # Assuming you have views in the listings app
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger API Documentation view
schema_view = get_schema_view(
   openapi.Info(
      title="ALX Travel App API",
      default_version='v1',
      description="API documentation for the ALX Travel App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@alxtravelapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

# Router for API views (assuming you have API views in the 'listings' app)
router = routers.DefaultRouter()
router.register(r'listings', views.ListingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.as_view(), name='swagger-docs'),  # Swagger documentation URL
    path('api/', include(router.urls)),  # Include API URLs
]

