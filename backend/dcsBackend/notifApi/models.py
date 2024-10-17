from django.db import models

class SMSNotification(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"SMS to {self.phone_number}"
