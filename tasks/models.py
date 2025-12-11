from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)  # False = incomplete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Default sort by newest