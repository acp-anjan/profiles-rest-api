from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test api view """

    def get(self, request, format=None):
        """Returns a list of Api features"""

        an_apiview =  [
            'Uses HTTP methods as functions (get, post,patch,put,delete)',
            'It is similar to traditional django view',
            'gives you the most control over the logic',
            'Is mapped manually to urls', 
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview}) 