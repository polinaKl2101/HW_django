from django.conf import settings
from django.core.mail import send_mail


def send_new_password(email, new_pass):
    send_mail(
        subject='Пароль изменен',
        message=f'Новый пароль для входа: {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )