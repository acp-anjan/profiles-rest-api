from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions
# Create your views here.

class HelloApiView(APIView):
    """Test api view """

    # making object of serializers
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of Api features"""

        an_apiview =  [
            'Uses HTTP methods as functions (get, post,patch,put,delete)',
            'It is similar to traditional django view',
            'gives you the most control over the logic',
            'Is mapped manually to urls', 
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview}) 

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                 status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """updates"""

        return Response({'method':'put'})

    
    def patch(self, request, pk=None):
        """updates some only"""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """deletes """
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """viewsets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'User action like (list, create, retrive, update)',
            'automatically maps to urls to routers',
            'provides more functionality with less code'
        ]

        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello string"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'HHello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({"http_method":"put"})

    def partial_update(self, request, pk=None):
        return Response({"http_method":"patch"})
    
    def destroy(self, request, pk=None):
        return Response({'http_method':'delete'})

class UserProfileViewset(viewsets.ModelViewSet):
    """ handling creating updating profiles"""

    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    permission_class = (permissions.UpdateOwnProfile,)
    authentication_class = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

