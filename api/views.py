from django.shortcuts import render
from .models import *
from .serializers import  *
from rest_framework.generics import ListCreateAPIView

class BotUsersApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer



class FeedbacksApiView(ListCreateAPIView):
    queryset = Feedbackk.objects.all()
    serializer_class = FeedbackSerializer


