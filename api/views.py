from rest_framework.generics import RetrieveAPIView
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response 
from .serializers import UserSerializer
User = get_user_model()


class UserDetailsView(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
