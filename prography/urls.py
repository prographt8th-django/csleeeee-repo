from .views import HumanLikeListView, HumanLikeCreateUpdateView, HumanListAPIView

from django.urls import path

urlpatterns = [
    path('human/', HumanListAPIView.as_view(), name='Human'),
    path('human_like/', HumanLikeListView.as_view(), name='HumanLike'),
    path('human_like/<int:pk>/',HumanLikeCreateUpdateView.as_view(), name='HumanLikeIt')
]
