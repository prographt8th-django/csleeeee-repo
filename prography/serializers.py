from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Human

class HumanSerializer(ModelSerializer):

	def validate(self, attrs):
		if attrs['likes'] != 0:
			raise ValidationError("I used redis cache, so I souldn't change it")
		return attrs
	class Meta:
		model = Human
		fields = '__all__'
