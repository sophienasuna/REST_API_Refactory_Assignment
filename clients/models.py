from django.db import models

# Create your models here.
# clients/models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.name