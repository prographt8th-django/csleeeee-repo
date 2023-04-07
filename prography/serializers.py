from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Human

class HumanSerializer(ModelSerializer):

	def validate(self, attrs):
		if attrs['likes'] != 0:
			raise ValidationError('기본 값이 0 이며 수정할 수 없습니다.')
		return attrs
	class Meta:
		model = Human
		fields = '__all__'
