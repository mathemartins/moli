from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from accounts.models import Profile
from accounts.utils import user_code_generator

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

User = get_user_model()

# Create your models here.

category_ = (
	("Tech", "Tech Automobile"),
	("Tech", "Tech Medical"),
	("Tech", "Tech Agriculture"),
	("Tech", "Tech Ecommerce"),
	("Tech", "Tech Computing")
)
	
status_ = (
	("StartUp", "StartUp"),
	("ScaleUp", "ScaleUp"),
)

stage_ = (
	("idea", "idea"),
	("research", "research"),
	("market validation", "market validation"),
	("revenue generation", "revenue generation"),
	("early growth", "early growth"),
	("expansion", "expansion"),
)

staff_count = (
	("1 - 5", "1 - 5"),
	("6 - 10", "6 - 10"),
	("Above 11+", "Above 11+"),
)

yes_no = (
	("YES", "YES"),
	("NO", "NO")
)

customer_count = (
	("1 - 10", "1 - 10"),
	("11 - 50", "51 - 150"),
	("151 - 500", "151 - 500"),
	("501 - 1,500", "501 - 1,500"),
	("1,501 - 10,000", "1,501 - 10,000"),
	("10,001 - More", "10,001 - More"),
)

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class StartUpQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True)


class StartUpManager(models.Manager):
	def queryset(self):
		return StartUpQuerySet(self.model, using=self._db)

	def all(self):
		return self.queryset().active()

	def featured(self):
		return self.queryset().featured()


class StartUp(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	company_name = models.CharField(max_length=200)
	category = models.CharField(choices=category_, max_length=100)
	stage = models.CharField(choices=stage_, max_length=100, blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	registered = models.BooleanField(default=False)
	users_or_customers = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	how_many_customers = models.CharField(choices=customer_count, blank=True, null=True, max_length=100)
	how_do_you_measure_growth = models.TextField(blank=True, null=True)
	why_are_you_in_business = models.TextField(blank=True, null=True)
	do_you_have_a_3_to_5_year_plan = models.CharField(max_length=100, blank=True, null=True, choices=yes_no)
	read_time = models.TimeField(null=True, blank=True)
	dashboard_image = models.ImageField(upload_to = upload_location, null = True, blank = True)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=100, blank=True, null=True)
	number_of_staffs = models.CharField(choices=staff_count, null=True, blank=True, max_length=100)
	active = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	slug = models.SlugField(null=True, blank=True)
	status = models.CharField(choices=status_, max_length=100)
	interest = models.ManyToManyField(User, blank=True, related_name='Interests')
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	objects = StartUpManager()

	class Meta:
		# db_table = "StartUp"
		verbose_name='StartUp'
		verbose_name_plural='StartUps'
		unique_together = ("company_name", "slug")
		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return self.company_name


def pre_save_signal(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.company_name)
		new_slug = "%s-%s" %(instance.company_name, instance.pk)
		try:
			slug_exists = StartUp.objects.get(slug=instance.slug)
			instance.slug = slugify(new_slug)
		except StartUp.DoesNotExist:
			instance.slug = instance.slug
		except StartUp.MultipleObjectsReturned:
			instance.slug = slugify(new_slug)
		except:
			pass

pre_save.connect(pre_save_signal, sender=StartUp)

roles = (
	("CEO", "CEO"),
	("CTO", "CTO"),
	("CFO", "CFO"),
	("COO", "COO"),
	("Engineer", "Engineer"),
	("Legal Adviser", "Legal Adviser"),
	("Manager", "Manager"),
	("Finance", "Finance"),
	("Business Developer", "Business Developer"),
	("Operator", "Operator"),
	("Others", "Others"),
)

years = (
	("1 - 5 years", "1 - 5 years"),
	("6 - 13 years", "6 - 13 years"),
	("14 - 20 years", "14 - 20 years"),
	("20 years and above", "20 years and above"),
)


class Team(models.Model):
	startup = models.ForeignKey(StartUp, on_delete=models.CASCADE, null=True, blank=True)
	role = models.CharField(choices=roles, blank=True, null=True, max_length=100)
	do_you_have_a_cofounder = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	how_many_cofounders = models.CharField(choices=staff_count, blank=True, null=True, max_length=100)
	do_you_have_an_communication_system = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	how_long_have_you_worked_together = models.CharField(choices=years, blank=True, null=True, max_length=100)
	do_you_have_a_legal_agreement_for_shareholders = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	list_the_functioning_units_in_your_business = models.TextField()
	do_you_have_human_resource_policy = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		db_table = "Team"
		verbose_name='StartUp Team'
		verbose_name_plural='StartUps Team'

	def __str__(self):
		return str(self.startup)


class Technology(models.Model):
	startup = models.ForeignKey(StartUp, on_delete=models.CASCADE, null=True, blank=True)
	does_your_business_require_technology = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	do_you_have_proprietor_technology_in_place = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		db_table = "Technology"
		verbose_name='StartUp Technology'
		verbose_name_plural = 'StartUps Technology '

	def __str__(self):
		return str(startup)


class Market(models.Model):
	startup = models.ForeignKey(StartUp, on_delete=models.CASCADE, null=True, blank=True)
	how_long_have_you_known_your_market = models.CharField(choices=years, blank=True, null=True, max_length=100)
	how_big_is_the_market_value = models.CharField(max_length=100, blank=True, null=True, default="$500,000")
	what_is_your_standout_point = models.CharField(max_length=100, blank=True, null=True, default="Mode Of Service Delivery")
	do_you_know_your_competitors = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	do_you_have_a_strategic_business_plan = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	mode_of_getting_target_audience = models.TextField() #front end box-checking
	social_media_presence = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		db_table = "Market"
		verbose_name='StartUp Market'
		verbose_name_plural = 'StartUps Market '

	def __str__(self):
		return str(startup)


class Finance(models.Model):
	startup = models.ForeignKey(StartUp, on_delete=models.CASCADE, null=True, blank=True)
	have_raised_fund_before = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	medium_of_fund_raising = models.CharField(max_length=100, blank=True, null=True) #family,friends,angel investors,shareholders
	do_you_have_fund_raising_plan = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	have_you_taking_a_loan_in_the_past = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	company_bank_account = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	financial_personnel = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	financial_record_updated = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	average_monthly_revenue = models.CharField(max_length=100, blank=True, null=True)
	average_monthly_expenditure = models.CharField(max_length=100, blank=True, null=True)
	future_year_forecast_financial_statement = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	cashflow_statement = models.CharField(choices=yes_no, blank=True, null=True, max_length=100)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		db_table = "Finance"
		verbose_name='StartUp Finance'
		verbose_name_plural = 'StartUps Finance '

	def __str__(self):
		return str(startup)

class Pitching(models.Model):
	startup = models.ForeignKey(StartUp, on_delete=models.CASCADE, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		db_table = "Pitch"
		verbose_name='StartUp Pitch'
		verbose_name_plural = 'StartUps Pitch '

	def __str__(self):
		return str(startup)

    


class InvestorManager(models.Manager):
	def all(self):
		return super(InvestorManager, self).filter(active=True)

class Investor(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
	job = models.CharField(max_length=100)
	description = models.TextField()
	active = models.BooleanField(default=True)
	slug = models.SlugField(null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	objects = InvestorManager()

	class Meta:
		verbose_name='Investor Data'
		verbose_name_plural='Investors Data'
		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return str(self.user)

