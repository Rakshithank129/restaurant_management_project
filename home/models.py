from django.db import models

# Create your models here.
class Restaurant(models.Model):
    """
    Restaurant models stores basic information of restaurants like name and description.
    """
    name = models.CharField(max_length=100)
    description= models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

        def __str__(self):
            return self.name
            

