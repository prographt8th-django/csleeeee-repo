from .models import Human

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.response import Response

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class HumanLikeListView(ListView):
    model = Human
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'likes')
        return ordering
    

class HumanLikeCreateUpdateView(CreateView, UpdateView):
    model = Human

    def get(self, request, *args: str, **kwargs):
        if 'likes' in cache:
            likes = cache.get('likes')
            return Response(likes)
        else:
            human = Human.objects.all()
            results = [h.to_json() for h in human]
            cache.set(human, results, timeout=CACHE_TTL)

    def post(self, request, *args: str, **kwargs):
        if 'likes' in cache:
            likes = cache.set('likes')
            return Response(likes)

