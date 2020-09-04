from django.db import models
# from datetime import datetime
from django.utils.timezone import datetime

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=150)
	date = models.DateTimeField(default=datetime.now(), blank=True)
	text = models.TextField(max_length=1000)
	image = models.ImageField(upload_to='blog_images/')
		

	def get_summary(self):
		return self.text[:70]

	def __str__(self):
		return self.title

	class Meta():
		"""docstring for Meta"""
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
			


	