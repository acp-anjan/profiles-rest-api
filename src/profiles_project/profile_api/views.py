from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import serializers
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