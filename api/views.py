from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Client

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)

    if user is not None:
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
    else:
        
        return Response({'error': 'Invalid credentials'}, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def count(request):
    
    query = request.query_params
    
    if query is not None:
        num = Client.objects.filter(**{param: value for param, value in query.items()}).count()
            
    else:
        num = Client.objects.all().count()
            
    return Response({'query': query, 'count': num})