from .models import Human
from .serializers import HumanSerializer

from django.shortcuts import HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class HumanListAPIView(APIView):
    @swagger_auto_schema(
        operation_id='GET Human',
        operation_description='Human 데이터를 가져옵니다.',
        query_serializer=HumanSerializer,
        tags=['Human']
    )
    def get(self, request):
        serializer = HumanSerializer(Human.objects.all(), many=True) # 정보를 가져올 때  Serializer 에서 검사한다.
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id='CREATE Human',
        operation_description='Human 데이터를 만듭니다.',
        request_body=HumanSerializer,
        tags=['Human']
    )
    def post(self, request):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 정보를 저장할 때 Serializer 에서 검사한다.
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class HumanLikeListView(ListView):
    model = Human
    paginate_by = 5
    
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
    

class HumanLikeDetailView(DetailView):
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
