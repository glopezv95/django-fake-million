from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Client
from .serializers import ClientSerializer

class ClientModelViewSet(viewsets.ModelViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
@api_view(['GET'])
def count(request):
    
    query = request.query_params
    
    if query is not None:
        num = Client.objects.filter(**{param: value for param, value in query.items()}).count()
            
    else:
        num = Client.objects.all().count()
            
    return Response({'query': query, 'count': num})