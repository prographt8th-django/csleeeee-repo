from rest_framework.serializers import ModelSerializer
from .models import Human

class HumanSerializer(ModelSerializer):
	class Meta:
		model = Human
		fields = '__all__'
