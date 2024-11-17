from django.db import models
from store.models.customer import Customer

class ChatMessage(models.Model):
    sender=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='sent_messages')
    receiver=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]

    class Meta:
        ordering = ('-timestamp',)

