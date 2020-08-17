from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import ProfileSerializer, OrderSerializer
from .models import Profile, Order

class SaveOrderAPIView(APIView):
    def post(self, request, format=None):
        items = request.data['items']
        store = request.data['store']
        # user = request.data['user']
        total = request.data['total']
        
        user = User.objects.get(pk=request.data['user'])
        order = Order(
            items=items,
            store=store,
            user=user,
            total=total
        )

        order.save()
        serialiazer = OrderSerializer(order)
        return Response(serialiazer.data)

class OrderListAPIView(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user__id=self.kwargs['user_id'])

class LoginAPIView(APIView):

    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            profile = Profile.objects.get(user=user)
            token = Token.objects.get(user=user)

            data = {
                'username': profile.user.username,
                'user': ProfileSerializer(profile).data,
                'token': token.key
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response('No es posible ingresar con esas credenciales', status=status.HTTP_404_NOT_FOUND)


class TokenAPIView(APIView):
    def post(self, request, format=None):
        key = request.data['key']
        token = Token.objects.get(key=key)
        profile = Profile.objects.get(user=token.user)

        data = {
            'username': profile.user.username,
            'user': ProfileSerializer(profile).data,
            'token': token.key
        }

        return Response(data, status=status.HTTP_202_ACCEPTED) 