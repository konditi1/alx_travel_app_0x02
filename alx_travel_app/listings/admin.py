from django.contrib import admin
from .models import Property, Booking, Payment

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'created_at')  # Use actual field names
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'booked_by', 'check_in', 'check_out')  # Use actual field names
    search_fields = ('booked_by', 'property__name')
    list_filter = ('check_in', 'check_out')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'transaction_id', 'status', 'amount', 'created_at')
    search_fields = ('transaction_id',)
    list_filter = ('status', 'created_at')
