from django.db import models
from accounts.models import User
import uuid

class Picture(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    prompt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)

    #connection to user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="picture", null=True)
