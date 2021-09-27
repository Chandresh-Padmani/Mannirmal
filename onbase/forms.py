from django import forms
from django.core.validators import RegexValidator, validate_email

GENDER_CHOICES = [('male', 'Male'), 
                  ('female', 'Female'), 
                  ('other', 'Other')]

class volunteer_form(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                               'id' : 'firstname', 
                                                               'class' : 'form-control form-control-alternative',
                                                               'placeholder' : 'First name', 
                                                               'name' : 'first_name'}))
                                # validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                #                            message='Please enter a valid name. Names may only contain alphabets.', 
                                #                            code='invalid')],
                                #  error_messages={'required': ''})
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                              'id' : 'lastname', 
                                                              'class' : 'form-control form-control-alternative',
                                                              'placeholder' : 'Last name', 
                                                              'name' : 'last_name'}))
                            #    validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                            #                               message='Please enter a valid name. Names may only contain alphabets.', 
                            #                               code='invalid_lastname')],
                            #     error_messages={'required': ''})                                             

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'id' : 'ip-datepicker', 
                                                                  'class' : 'form-control form-control-alternative js-datepicker',
                                                                  'placeholder' : 'YYYY-MM-DD', 
                                                                  'name' : 'date_of_birth',
                                                                  'maxlength': '0'}), required=True)
                                    # error_messages={'required': '*'})
    
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES), required=True) 
                            #  error_messages={'required': '*'})                        
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type' : 'email',
                                                           'id' : 'email', 
                                                           'class' : 'form-control form-control-alternative',
                                                           'placeholder' : 'jesse@example.com', 
                                                           'name' : 'email'}))
                            # validators=[validate_email],
                            #  error_messages={'required': ''})
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'id' : 'number', 
                                                                 'class' : 'form-control form-control-alternative',
                                                                 'placeholder' : '9999999999', 
                                                                 'name' : 'phone_number'}), required=True)
                                #    max_length=10,
                                #    validators=[RegexValidator(regex='^([0-9]{5,15})+$', 
                                #                               message='Please enter a valid phone number. Phone numbers may only contain numbers', 
                                #                               code='invalid_phonenumber')],
                                #    error_messages={'required': ''})
    
    address = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                            'id' : 'address', 
                                                            'class' : 'form-control form-control-alternative',
                                                            'placeholder' : 'eg, Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09', 
                                                            'name' : 'address'}), required=True)
                            #   max_length=100,
                            #   error_messages={'required': ''})

    city = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                         'id' : 'city', 
                                                         'class' : 'form-control form-control-alternative',
                                                         'placeholder' : 'eg. New York', 
                                                         'name' : 'city'}), required=True)
                        #    max_length=30,
                        #    validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                        #                               message='Please enter a valid city. City names may only contain alphabets.', 
                        #                               code='invalid_city')],
                        #    error_messages={'required': ''})
    
    country = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                            'id' : 'country', 
                                                            'class' : 'form-control form-control-alternative',
                                                            'placeholder' : 'United States', 
                                                            'name' : 'country'}), required=True)
                            #   max_length=30,
                            #   validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                            #                              message='Please enter a valid country. Country names may only contain alphabets.', 
                            #                              code='invalid_country')],
                            #   error_messages={'required': ''})
    
    postal_code = forms.CharField(widget=forms.TextInput(attrs={
                                                                'id' : 'postal', 
                                                                'class' : 'form-control form-control-alternative',
                                                                'placeholder' : '999999', 
                                                                'name' : 'postal_code'}),required=True)
                                #   max_length=6,
                                #   validators=[RegexValidator(regex='^([0-9]{0,5})+$', 
                                #                              message='Please enter a valid postal code. Postal code may only contain numbers', 
                                #                              code='invalid_postalcode')],
                                #   error_messages={'required': ''})
    
    description = forms.CharField(widget=forms.Textarea(attrs={'type' : 'text',
                                                               'id' : 'description', 
                                                               'class' : 'form-control form-control-alternative',
                                                               'placeholder' : 'A few words about you ...', 
                                                               'name' : 'description',
                                                               'rows' : '4',
                                                               'resize' : 'none'}), required=False)
                                # validators=[RegexValidator(regex='^[a-zA-Z0-9\'":()&$%-_@+#*=.;,?!\s]*$', 
                                #                              message='Only the following special characters are allowed: ,.?!;\'"', 
                                #                              code='invalid_description')],
                                # max_length=500,
                                # required=False)                                

class ideas_form(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                               'id' : 'idea-firstname', 
                                                               'class' : 'form-control form-control-alternative',
                                                               'placeholder' : 'John',
                                                               'name' : 'first_name'}))
                                #  validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                #                             message='Please enter a valid name. Names may only contain alphabets.', 
                                #                             code='invalid_firstname')],
                                #  error_messages={'required': ''})
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type' : 'text',
                                                              'id' : 'idea-lastname', 
                                                              'class' : 'form-control form-control-alternative',
                                                              'placeholder' : 'Doe', 
                                                              'name' : 'last_name'}))
                                # validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                #                            message='Please enter a valid name. Names may only contain alphabets.', 
                                #                            code='invalid_lastname')],
                                # error_messages={'required': ''})                      
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type' : 'email',
                                                            'id' : 'idea-email', 
                                                            'class' : 'form-control form-control-alternative',
                                                            'placeholder' : 'jesse@example.com', 
                                                            'name' : 'email'}))
                            #  validators=[validate_email],
                            #  error_messages={'required': ''})
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
                                                                 'id' : 'idea-number', 
                                                                 'class' : 'form-control form-control-alternative',
                                                                 'placeholder' : '999 999 9999', 
                                                                 'name' : 'phone_number'}), required=True)
                                #    max_length=10,
                                #    validators=[RegexValidator(regex='^([0-9]{5,15})+$', 
                                #                               message='Please enter a valid phone number. Phone numbers may only contain numbers', 
                                #                               code='invalid_phonenumber')],
                                #    error_messages={'required': ''})
    
    feedback = forms.CharField(widget=forms.Textarea(attrs={'type' : 'text',
                                                            'id' : 'idea-feedback', 
                                                            'class' : 'form-control form-control-alternative',
                                                            'placeholder' : 'A few words about our service ...', 
                                                            'name' : 'feedback',
                                                            'rows' : '4',
                                                            'resize' : 'none'}), required=False)
                            #    validators=[RegexValidator(regex='^[a-zA-Z0-9\'":()&$%-_@+#*=.;,?!\s]*$', 
                            #                               message='Only the following special characters are allowed: ,.?!;\'"', 
                            #                               code='invalid_feedback')],
                            #    max_length=500,
                            #    required=False)     
    
    thoughts = forms.CharField(widget=forms.Textarea(attrs={'type' : 'text',
                                                            'id' : 'idea-thoughts', 
                                                            'class' : 'form-control form-control-alternative',
                                                            'placeholder' : 'Share your ideas and new thoughts about our activities and foundation ...', 
                                                            'name' : 'thoughts',
                                                            'rows' : '4',
                                                            'resize' : 'none'}))
                            #    validators=[RegexValidator(regex='^[a-zA-Z0-9\'":()&$%-_@+#*=.;,?!\s]*$', 
                            #                               message='Only the following special characters are allowed: ,.?!;\'"', 
                            #                               code='invalid_thoughts')],
                            #    max_length=500,
                            #    required=False)                              