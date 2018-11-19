from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class dairyNode(models.Model):
	Name 		=	models.ForeignKey(User, on_delete= models.CASCADE)
	Quantity_of_milk = models.FloatField()
	Date		=	models.DateTimeField(auto_now_add=True)
	Person_Name = 	models.CharField(max_length=15)

	def __str__(self):
		return self.Name.username