from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def send_contact_email(mail_subject, mail_template, context):
    to_email = settings.EMAIL_HOST_USER
    message = render_to_string(mail_template, context)
    from_email = context["email"]
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()
