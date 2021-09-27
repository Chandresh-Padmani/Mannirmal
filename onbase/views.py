from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.validators import validate_slug, validate_email

from django.template.defaultfilters import date
from urllib.parse import urlencode
from django.urls import reverse

from onbase.models import vol_model, ideas_model, count_model, donors_model

from datetime import date

from .forms import volunteer_form, ideas_form

from django.conf import settings 

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Image

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .token_generator import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

def index(request):
    counts = count_model.objects.all()
    donors = donors_model.objects.all()
    return render(request, 'index.html', {"counts":counts, "donors":donors})

def about(request):
    return render(request, 'about.html')

def volunteer(request):
    if request.method == "POST":

        form = volunteer_form(request.POST)

        if form.is_valid():

            volunteer_res = vol_model.objects.all()
            account_exists = False

            for vol in volunteer_res:
                if vol.email == request.POST.get('email'):
                    account_exists = True
                    break
            
            if account_exists:

                base_url = reverse('success')
                query_string =  urlencode({'from': 'volunteer-exists'})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
                
            else:

                new_vol = vol_model(first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), 
                                    date_of_birth = request.POST.get('date_of_birth'), gender = request.POST.get('gender'), 
                                    email = request.POST.get('email'), 
                                    phone_number = '+' + request.POST.get('country_code') + ' ' + request.POST.get('phone_number'), 
                                    address = request.POST.get('address'), city = request.POST.get('city'), country = request.POST.get('country'), 
                                    postal_code = request.POST.get('postal_code'), description = request.POST.get('description'))
                new_vol.is_active = False
                new_vol.save()

                subject, from_email, to = 'welcome', settings.EMAIL_HOST_USER, request.POST.get('email')

                html_content = get_template('confirmation_email.html').render(
                               { 'username': request.POST.get('first_name') + ' ' + request.POST.get('last_name'),
                                 'email': request.POST.get('email'),
                                 'uid': urlsafe_base64_encode(force_bytes(new_vol.id)),
                                 'domain': get_current_site(request).domain,
                                 'token': account_activation_token.make_token(new_vol)})

                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                base_url = reverse('success')
                query_string =  urlencode({'from': 'volunteer'})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
    else:
        form = volunteer_form()
    
    qs = vol_model.objects.filter(date_of_birth__day = date.today().day).filter(date_of_birth__month = date.today().month)

    return render(request, 'volunteer.html', {'form' : form,
                                              'qs' : qs,})


def portfolio(request):
    pics = Image.objects.all()
    return render(request, 'portfolio.html', {"pics": pics})

def team(request):
    return render(request, 'team.html')

def ideas(request):
    if request.method == "POST" or not request.is_ajax():
        form = ideas_form(request.POST)
        if form.is_valid():
            new_ideas = ideas_model(first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'),
                                    email = request.POST.get('email'), 
                                    phone_number = '+' + request.POST.get('country_code') + ' ' + request.POST.get('phone_number'), 
                                    feedback = request.POST.get('feedback'), thoughts = request.POST.get('thoughts'))
            new_ideas.save()

            # username = request.POST['first_name']
            # email = request.POST['email']

            # htmly = get_template('Email.html')
            # d = { 'username': username }
            # subject, from_email, to = 'welcome', 'wizmrcomputer@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            # ################################################################## 
            # messages.success(request, f'Your account has been created !')

            base_url = reverse('success')
            query_string =  urlencode({'from': 'ideas'})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = ideas_form()
    
    req_errors = {'first_name_req_error': "*",
                  'last_name_req_error': "*",
                  'email_req_error': "*",
                  'phone_number_req_error': "*"}

    inv_errors = {'first_name_inv_error': "",
                  'last_name_inv_error': "",
                  'email_inv_error': "",
                  'phone_number_inv_error': ""}
    
    for x in ['first_name', 'last_name', 'email', 'phone_number']:
        if form.errors.get(x) is not None:
            if form.errors.get(x).as_text() != "* ":
                req_errors[x + '_req_error'] = ""
                inv_errors[x + '_inv_error'] = form.errors.get(x).as_text()
    
    return render(request, 'ideas.html', {'form' : form,
                                          'req_errors': req_errors,
                                          'inv_errors': inv_errors})

def contact(request):
    return render(request, 'contact.html')

def donate(request):
    return render(request, 'donate.html')

def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        volunteer = vol_model.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, vol_model.DoesNotExist):
        volunteer = None
    if volunteer is not None and account_activation_token.check_token(volunteer, token):
        volunteer.is_active = True
        volunteer.save()
        header =  'Thank you!'
        text = 'Congratulations! You have successfully registered as a volunteer in the Mannirmal Foundation.' 
        return render(request, 'success.html', {'header': header,
                                                'text': text})
    else:
        header =  '???'
        text = 'Activation link is invalid!' 
        return render(request, 'success.html', {'header': header,
                                                'text': text})

def success(request):
    if request.GET.get('from') == 'volunteer':
        header =   'You\'re almost there!'
        text = 'Please go to your submitted e-mail address. A mail from the foundation will be there to confirm your application.'
    elif request.GET.get('from') == 'volunteer-exists':
        header =  'You are already one of us!'
        text = 'Your given email is already registered as a volunteer.'
    elif request.GET.get('from') == 'ideas':
        header =  'Thank you!'
        text = 'Your feedback and suggestions mean the world to us. Thank you very much for your time and energy.'  

    return render(request, 'success.html', {'header': header,
                                            'text': text})
