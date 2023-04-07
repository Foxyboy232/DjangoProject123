from django.core.mail import send_mail


def send_email(subject: str, body: str, recipients: list, sender_email: str = "test@gmail.com"):
    send_mail(
        subject,
        body,
        sender_email,
        recipients,
        fail_silently=False)