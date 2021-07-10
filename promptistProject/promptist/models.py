from django.db import models
import uuid

class Picture(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    prompt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')

