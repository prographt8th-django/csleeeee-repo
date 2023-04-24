from django.test import TestCase

from .models import Human


class HumanTestCase(TestCase):
    def setUp(self):
        Human.objects.create(name="cslee", description="healthful guy", likes=0)

    def test_human_name(self):
        human = Human.objects.get(pk=1)
        self.assertEqual(human.name, 'cslee')
