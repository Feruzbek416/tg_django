from .models import BotUser, Feedbackk
from rest_framework.serializers import ModelSerializer

class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('name','username','user_id','created_at')


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedbackk
        fields = ('user_id','created_at','body','age','name','surname','school')

