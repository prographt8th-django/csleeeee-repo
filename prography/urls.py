from .views import HumanLikeListView, HumanLikeCreateUpdateView

from django.urls import path

urlpatterns = [
    path('human_like/', HumanLikeListView.as_view(), name='HumanLike'),
    path('human_like/<int:pk>/',HumanLikeCreateUpdateView.as_view(), name='HumanLikeIt')
]
