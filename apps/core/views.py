import requests

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



class PaceSetter (APIView):
    def post(self, request, format=None):
        url = 'http://189.223.128.30:8081/'
        headers = {'Content-Type': 'text/xml'}
        xml = request.data['xml']
        r = requests.post(url, xml, headers=headers)

        print(r.text)

        return Response(r.text)