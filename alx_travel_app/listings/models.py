from django.db import models
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    booked_by = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.booked_by}"

