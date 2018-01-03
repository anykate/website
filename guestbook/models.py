from django.db import models

# Create your models here.
class Comment(models.Model):
	name = models.CharField(max_length=20)
	comment = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'Name: {}; ID:{}'.format(self.name, self.id)
