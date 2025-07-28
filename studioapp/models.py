from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Work(models.Model):
    caption=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='contact_photos/', blank=True, null=True)
    def __str__(self):
        return self.caption
# class Booking_list(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     location = models.CharField(max_length=300, blank=True)
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} - {self.email}"