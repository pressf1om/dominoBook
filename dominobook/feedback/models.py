from django.db import models


class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания фидбека автоматически заполняется при создании

    def __str__(self):
        return f"Feedback from {self.email} at {self.created_at}"
