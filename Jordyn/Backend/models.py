from django.db import models

# Create your models here.
class Instruction(models.Model):
    spice = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    pub_date = models.DateTimeField('date published')
