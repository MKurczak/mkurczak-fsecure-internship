from django.db import models

# Create / initialize DB.
class listModel(models.Model):
    randomEntry = models.CharField(max_length=120)
    anotherRandomEntry = models.CharField(max_length=120)