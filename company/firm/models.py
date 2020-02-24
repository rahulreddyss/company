from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Departments(models.Model):
	name = models.CharField(max_length=100)
	dpet_no = models.IntegerField(default=0.0)

	def __unicode__(self):
		return self.name


class Employees(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	department = models.ForeignKey(Departments, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, null=True, blank=True)
	employee_no = models.IntegerField()
	mobile = models.IntegerField()
	country = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	pincode = models.IntegerField()
	salary = models.FloatField(default=0.0)
	slug = models.SlugField(unique=True, null=True, blank=True)

	def __unicode__(self):
		return self.user.first_name

	def get_absolute_url(self):
		return reverse("firm:detail", kwargs={"slug": self.slug})

	def get_api_url(self):
		return reverse("firm-api:detail", kwargs={"slug": self.slug})


	def create_slug(instance, new_slug=None):
		slug = slugify(instance.title)
		if new_slug is not None:
			slug = new_slug
		qs = Employees.objects.filter(slug=slug).order_by("-id")
		exists = qs.exists()
		if exists:
			new_slug = "%s-%s" %(slug, qs.first().id)
			return create_slug(instance, new_slug=new_slug)
		return slug