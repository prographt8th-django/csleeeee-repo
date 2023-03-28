from .models import Human

from django.shortcuts import render, HttpResponse
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
    
    def get(self, request, *args, **kwargs):
        human = Human.objects.all()
        for h in human:
            cache.get(h.id)
            print(cache.get(h.id))

        return super().get(request, *args, **kwargs)
    

class HumanLikeCreateUpdateView(CreateView, UpdateView):
    model = Human

    def get(self, request, *args: str, **kwargs):
        human_id = kwargs['pk']

        if cache.get(human_id):
            likes = cache.get(human_id)
            print("get cache", likes)
        else:
            try:
                obj = Human.objects.get(pk=human_id)
                cache.set(human_id, obj.likes + 1, timeout=CACHE_TTL)
                print("set cache")
            except Human.DoesNotExist:
                return HttpResponse("Does not exist")
            return HttpResponse("Ok")
        return HttpResponse("Correctly")
