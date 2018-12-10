from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=50)

    class Meta:
        pass

class Skill(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    class Meta:
        pass