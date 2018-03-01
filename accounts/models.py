from django.db import models
from django.db.models.signals import pre_save, post_save

from django.contrib.auth import get_user_model

from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.utils import timezone

# Create your models here.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from accounts.utils import user_code_generator

User = get_user_model()

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

gender_ = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Other', 'Other'),
	)

years = (
	("1 - 5 years", "1 - 5 years"),
	("6 - 13 years", "6 - 13 years"),
	("14 - 20 years", "14 - 20 years"),
	("20 years and above", "20 years and above"),
)

UserType = (
	("Investor", "Investor"),
	("StartUp", "StartUp"),
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	user_code = models.CharField(max_length=5)
	user_type = models.CharField(choices=UserType, blank=True, null=True, max_length=100)
	image = ProcessedImageField(upload_to=upload_location, processors=[ResizeToFill(150, 150)], 
								format='JPEG', options={'quality':100}, null=True, blank=True)
	is_member = models.BooleanField(default=False, verbose_name="Premium Account")
	skill_set = models.CharField(default="I don't have any.", max_length=100)
	years_of_experience = models.CharField(choices=years, blank=True, null=True, max_length=100)
	mobile_number = models.CharField(max_length=11)
	street = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	state = models.CharField(max_length=100, blank=True, null=True)
	zip_code = models.CharField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=100, blank=True, null=True)
	gender = models.CharField(choices=gender_, max_length=100)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	# objects = ProfileManager()

	class Meta:
		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return str(self.user)


def new_user_signal(sender, instance, created, *args, **kwargs):
	pass

