from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Property(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)  # Available or not
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )

    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        num_nights = (self.check_out - self.check_in).days
        self.total_cost = num_nights * self.property.price_per_night
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.booked_by.username} for {self.property.name}"


class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="payment")
    transaction_id = models.CharField(max_length=100, blank=True, null=True, unique=True)  # Chapa provides a string-based ID
    chapa_reference = models.CharField(max_length=100, blank=True, null=True, unique=True)  # Store Chapa reference ID
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track updates

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.status}"
