from django.test import TestCase

from .models import Human
from config.exceptions import exception


class HumanTestCase(TestCase):
    def setUp(self):
        Human.objects.create(name="cslee", description="healthful guy", likes=0)

    def test_human_name(self):
        human = Human.objects.get(pk=1)
        self.assertEqual(human.name, 'cslee')

    def test_human_likes_exception_onlycache(self):
        with self.assertRaises(exception.OnlyCache):
            Human.objects.create(name="kim", description="kimchi", likes=1)
