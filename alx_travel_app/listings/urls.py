from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, BookingViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)  # Changed from 'listings' to 'properties'
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)  # Added payment endpoint

urlpatterns = [
    path('api/', include(router.urls)),
]
