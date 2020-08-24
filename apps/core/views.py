import requests

from b2bmayoreoapi.settings.base import EMAIL_HOST_USER

from django.core.mail import send_mail

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string

class SendEmail(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        order_number = request.data['orderNumber']
        subject = 'Ref del valle'
        message = 'Mensaje del email'
        # context = Context({'username': username})    
        context = {'order_number': order_number}
        html_content = render_to_string('email.html', context)

        email = EmailMultiAlternatives(subject=subject, from_email=EMAIL_HOST_USER, to=[email,])
        # email = EmailMultiAlternatives(subject=subject, from_email=EMAIL_HOST_USER)
        email.attach_alternative(html_content, 'text/html')
        # email.to = [email]
        email.send()
        # send_mail(subject,
        #     message, EMAIL_HOST_USER, [email], fail_silently=False)

        return Response('success')

class PaceSetter(APIView):
    def post(self, request, format=None):
        url = 'http://189.223.128.30:8081/'
        headers = {'Content-Type': 'text/xml'}
        xml = request.data['xml']
        r = requests.post(url, xml, headers=headers)

        print(r.text)

        return Response(r.text)