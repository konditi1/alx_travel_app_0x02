from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Property, Booking, Payment
from .serializers import PropertySerializer, BookingSerializer, PaymentSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    """ViewSet for managing property listings."""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create/update properties

    def perform_create(self, serializer):
        """Assigns the currently logged-in user as the host."""
        serializer.save(host=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for handling bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can book

    def perform_create(self, serializer):
        """Auto-assigns the currently logged-in user as the guest making the booking."""
        serializer.save(booked_by=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for handling payments."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can pay

    def perform_create(self, serializer):
        booking = serializer.validated_data.get('booking')
        serializer.save(booking=booking)
