from rest_framework.serializers import ModelSerializer
from companies.models import StartUp, Investor
from accounts.models import Profile


class StartUpCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = StartUp
		fields = [
			"company_name",
			"category",
			"description",
			"address",
			"status",
			"stage",
			"registered",
			"users_or_customers",
			"how_many_customers",
			"how_do_you_measure_growth",
			"why_are_you_in_business",
			"do_you_have_a_3_to_5_year_plan",
			"city",
			"country",
			"number_of_staffs",
		]

	def create(self, validated_data):
		user = None
		request = self.context.get("request")
		if request and hasattr(request, "user"):
			user = request.user
		user_profile = Profile.objects.get(user=user)

		instance = StartUp.objects.create (
			user = user_profile,
			company_name = self.validated_data['company_name'],
			category = self.validated_data['category'],
			description = self.validated_data['description'],
			address = self.validated_data['address'],
			status = self.validated_data['status']
		)
		return instance


class StartUpDetailSerializer(ModelSerializer):
	class Meta:
		model = StartUp
		fields = [
			"user",
			"pk",
			"company_name",
			"category",
			"description",
			"read_time",
			"dashboard_image",
			"address",
			"active",
			"featured",
			"slug",
			"status",
			"interest",
			"updated",
			"timestamp",
		]



class StartUpListSerializer(ModelSerializer):
	class Meta:
		model = StartUp
		fields = [
			"company_name",
			"category",
			"description",
			"dashboard_image",
			"address",
		]



class InvestorSerializer(ModelSerializer):
	class Meta:
		model = Investor
		fields = [
			"user",
			"startup",
			"job",
			"description",
			"active",
			"slug",
			"updated",
			"timestamp",
		]