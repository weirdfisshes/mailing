from main.models import Client, Mailing, Message
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
