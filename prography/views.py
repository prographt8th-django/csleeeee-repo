from .models import Human

from django.shortcuts import render
from django.views.generic import ListView


class HumanLikeListView(ListView):
    model = Human
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'likes')
        return ordering
