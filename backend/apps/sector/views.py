from haystack.query import SearchQuerySet
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .models import Sector
from .serializers import SectorSerializer


class SectorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

    @list_route(methods=['get'])
    def autocomplete(self, request):
        AUTOCOMPLETE_SIZE = 10
        query = request.GET.get('q', '')
        if not query:
            sqs = Sector.objects.none()
        else:
            sqs = SearchQuerySet()\
                .filter(name_auto=query, standardized=True)\
                .models(Sector)[:AUTOCOMPLETE_SIZE]
        serializer = self.get_serializer(sqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
