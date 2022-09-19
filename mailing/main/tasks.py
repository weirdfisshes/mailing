import datetime

import pytz
import requests
from django.conf import settings

from mailing.celery import app

from .models import Client, Mailing, Message


@app.task(bind=True, retry_backoff=True)
def send_message(
    self, data, client_id, mailing_id,
    url=settings.URL, token=settings.URL
):
    mailing = Mailing.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.time_zone)
    now = datetime.datetime.now(timezone)

    if mailing.start_date <= now <= mailing.stop_date:
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
            print('Сообщение отправлено')
        except requests.exceptions.RequestException as exc:
            print('Сообщение не отправлено, попробуем позже')
            raise self.retry(exc=exc)
        else:
            Message.objects.filter(pk=data['id']).update(status='sent')
