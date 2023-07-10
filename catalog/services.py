from django.core.mail import send_mail
from catalog.models import Mailing, Log, Message
from django.core.cache import cache
from config import settings


def daily_mailing():
    for i in Mailing.objects.filter(frequency='daily'):
        i.status = 'started'
        i.save()
        send_mail(i)
        i.status = 'completed'
        i.save()


def weekly_mailing():
    for i in Mailing.objects.filter(frequency='weekly'):
        i.status = 'started'
        i.save()
        send_mail(i)
        i.status = 'completed'
        i.save()


def monthly_mailing():
    for i in Mailing.objects.filter(frequency='monthly'):
        i.status = 'started'
        i.save()
        send_mail(i)
        i.status = 'completed'
        i.save()


def send_mail(message):
    clients_emails = message.clients.values_list('email', flat=True)

    for email in clients_emails:
        message = Message.objects.create(message=message)
        try:
            send_mail(
                message.title,
                message.body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            status = 'success'
            server_response = 'Письмо отправлено!'
        except Exception as e:
            status = 'error'
            server_response = str(e)
        Log.objects.create(message=message, status=status, server_response=server_response)


def get_cache_log(log):
    if settings.CACHE_ENABLED:
        cache_key = f'log_{log.pk}'
        cached_data = cache.get(cache_key)
        if cached_data is None:
            cached_data = {
                'message': log.message,
                'timedata': log.timedata,
                'status': log.status,
                'server_response': log.server_response,
            }
            cache.set(cache_key, cached_data, 120)
        return cached_data
    else:
        return {
            'message': log.message,
            'timedata': log.timedata,
            'status': log.status,
            'server_response': log.server_response,
        }