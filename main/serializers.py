from django.contrib.auth.models import User
from main.models import Messages
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('content', 'send_from', 'send_to', 'datetime', )
