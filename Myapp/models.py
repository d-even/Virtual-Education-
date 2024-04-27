from django.db import models

class Cookie(models.Model):
    Name = models.CharField( max_length=50)
    Email = models.CharField( max_length=50)
    Phone = models.CharField( max_length=50)

    def __str__(self):
        return self.Name