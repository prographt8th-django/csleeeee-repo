from django.test import TestCase
from django.core.serializers import serialize
from unittest.mock import Mock, MagicMock

from .models import Human


class HumanTestCase(TestCase):
    def setUp(self):
        Human.objects.create(name="cslee", description="healthful guy", likes=0)
        # Human.objects.create(name="AI", description="healthful AI", likes=99)

    def test_queryset_exists(self):
        qs = Human.objects.all()
        self.assertTrue(qs.exists)

    def test_queryset_correct(self):
        qs = Human.objects.get(name="cslee")
        self.assertEqual(qs.name, "cslee")
