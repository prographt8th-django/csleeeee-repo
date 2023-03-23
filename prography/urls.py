from .views import HumanLikeListView

from django.urls import path

urlpatterns = [
    path('human_like/', HumanLikeListView.as_view(), name='HumanLike'),
]
