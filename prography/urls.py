from .views import HumanLikeListView, HumanLikeDetailView, HumanListAPIView, HumanDetailAPIView

from django.urls import path

urlpatterns = [
    path('human/', HumanListAPIView.as_view(), name='Human'),
    path('human/<int:pk>/', HumanDetailAPIView.as_view(), name='HumanDetail'),

    path('human_like/', HumanLikeListView.as_view(), name='HumanLike'),
    path('human_like/<int:pk>/',HumanLikeDetailView.as_view(), name='HumanLikeIt')
]
