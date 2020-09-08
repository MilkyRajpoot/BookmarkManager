from django.db import models
from geolocation_fields.models import fields

# Create your models here.

class Customer(models.Model):
	location = fields.PointField(verbose_name='Point',null=True,blank=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ('created_at',)

	def __str__(self):
		return str(self.location)

class Bookmark(models.Model):
	title = models.CharField(max_length=255)
	url = models.URLField(verbose_name="Link", max_length=1000)
	source_name = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ('created_at',)

	def __str__(self):
		return self.title + " : " + str(self.source_name)

class CustomerBookmark(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
	bookmark = models.ForeignKey(Bookmark,on_delete=models.CASCADE,null=True,blank=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ('created_at',)

	def __str__(self):
		return self.created_at



