from django.test import TestCase
from django.core.serializers import serialize
from unittest.mock import Mock, MagicMock

from .models import Human


class HumanTestCase(TestCase):
    def test_queryset_exists(self):
        qs = Human.objects.all()
        self.assertTrue(qs.exists)