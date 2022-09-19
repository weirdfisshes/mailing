import pytz
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Client(models.Model):
    TIMEZONE_CHOICES = zip(pytz.all_timezones, pytz.all_timezones)
    phone_regex = RegexValidator(
        regex=r'^7\d{10}$',
        message="Номер должен быть в формате 7XXXXXXXXXX, Х - цифра от 0 до 9"
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        validators=[phone_regex],
        max_length=11,
        unique=True
    )
    mobile_code = models.CharField(
        verbose_name='Код мобильного оператора',
        max_length=3
    )
    tag = models.CharField(verbose_name='Тег', max_length=100, blank=True)
    time_zone = models.CharField(
        verbose_name='Часовой пояс',
        max_length=50,
        default='UTC',
        choices=TIMEZONE_CHOICES
    )

    def __str__(self):
        return f'Клиент: {self.id}, номер: {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    start_date = models.DateTimeField(verbose_name='Начало рассылки')
    stop_date = models.DateTimeField(verbose_name='Конец рассылки')
    text = models.TextField(max_length=255, verbose_name='Message text')
    mobile_code = models.CharField(
        verbose_name='Код мобильного оператора',
        max_length=3
    )
    tag = models.CharField(verbose_name='Тег', max_length=100, blank=True)

    @property
    def sending(self):
        now = timezone.now()
        if self.start_date <= now <= self.stop_date:
            return True
        else:
            return False

    def __str__(self):
        return (f'Рассылка: {self.id}, '
                f'начало: {self.start_date}, '
                f'конец: {self.stop_date}')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    SENT = "sent"
    NOT_SENT = "not sent"
    STATUS_CHOICES = [
        (SENT, "Отправлено"),
        (NOT_SENT, "Не отправлено"),
    ]
    created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    status = models.CharField(
        verbose_name='Статус отправки',
        max_length=20,
        choices=STATUS_CHOICES
    )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    def __str__(self):
        return (f'Рассылка: {self.mailing}, '
                f'клиент:{self.client}, '
                f'статус: {self.status}')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
