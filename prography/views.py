from .models import Human

from django.shortcuts import HttpResponse, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class HumanLikeListView(ListView):
    model = Human
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'likes')
        return ordering
    
    def get(self, request, *args, **kwargs):
        objects = Human.objects.all()
        for obj in objects:
            if cache.get(obj.id) is None:
                """
                timeout=600, if you use your time (600s), clear the cache
                cache value desc: {obj.id: obj.likes}
                """
                cache.set(obj.id, obj.likes, timeout=600)
            else:
                pass

        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = context['object_list']

        cache_dict = {}
        for obj in objects:
            cache_dict[obj.id] = cache.get(obj.id)

        context['cache_likes'] = cache_dict
        
        return context
    

class HumanLikeCreateUpdateView(CreateView, UpdateView):
    model = Human

    def get(self, request, *args: str, **kwargs):
        human_id = kwargs['pk']

        if cache.get(human_id) is not None:
            try:
                cache.incr(human_id)
            except Human.DoesNotExist:
                return HttpResponse("Except Does not exist")
            return redirect("HumanLike")
        return HttpResponse("If Does not exist")
