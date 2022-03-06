from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
