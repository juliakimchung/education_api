from django.db import models

# Create your models here.
class Course(models.Model):
	description=models.TextField()
	title = models.CharField(max_length=250)

	def __str__(self):
		return self.title

class Review(models.Model):
	course = models.ForeignKey(Course, related_name='reviews')
	name = models.CharField(max_length=225)
	email = models.EmailField()
	comment = models.TextField(blank=True, default="")
	rating = models.IntegerField()

	class Meta:
		unique_together = ['email', 'course']

	def __str__(self):
		return '{0.rating} by {0.email} for {0.course}'.format(self)