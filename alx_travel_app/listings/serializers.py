from rest_framework import serializers
from .models import Property, Booking, Payment

# Property Serializer (formerly ListingSerializer)
class PropertySerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField()  # Show host's username instead of ID

    class Meta:
        model = Property
        fields = '__all__'


# Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    booked_by = serializers.StringRelatedField()  # Show guest's username
    property = PropertySerializer(read_only=True)  # Nested property details

    class Meta:
        model = Booking
        fields = '__all__'


# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(), write_only=True)
    booking_details = BookingSerializer(source="booking", read_only=True)


    class Meta:
        model = Payment
        fields = '__all__'
