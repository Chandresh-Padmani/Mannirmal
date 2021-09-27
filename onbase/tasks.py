from django.conf import settings 

from celery import shared_task, Celery

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from datetime import date

from onbase.models import vol_model

@shared_task
def send_birthday_emails():
    
    qs = vol_model.objects.filter(date_of_birth__day = date.today().day).filter(date_of_birth__month = date.today().month).filter(is_active = True)
    emails = {}

    for result in qs: 
        emails[result.email] = {}
        emails[result.email]['username'] = result.first_name + " " + result.last_name
    
    subject, from_email = 'REGARDING SEMESTER 5 RESULT', settings.EMAIL_HOST_USER
    
    for email in emails:
        to = email

        html_content = get_template('birthday_email.html').render({'username': emails[email]['username']})
        
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
