from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

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

@api_view(['POST'])
def login(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)

    if user is not None:
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
    else:
        
        return Response({'error': 'Invalid credentials'}, status=400)