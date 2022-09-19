from django.shortcuts import get_object_or_404
from main.models import Client, Mailing, Message
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk):
        queryset = Mailing.objects.all()
        get_object_or_404(queryset, pk=pk)
        queryset = Message.objects.filter(mailing_id=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def total(self, request):
        total = Mailing.objects.count()
        mailings = Mailing.objects.values('id')
        details = {}
        for mailing in mailings:
            amount = Message.objects.filter(mailing_id=mailing['id']).all()
            details[mailing['id']] = {
                'Всего писем': amount.count(),
                'Доставлено': amount.filter(status='Sent').count(),
                'Не доставлено': amount.filter(status='Not sent').count()
            }
        content = {'Всего рассылок': total, 'Письма': details}
        return Response(content)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
