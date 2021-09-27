from django.core.validators import RegexValidator, validate_email
from django.core.exceptions import ValidationError
# from django.db.models import DEFERRED

from django.db import models
from django.contrib import admin


class Image(models.Model):
    cover = models.FileField(upload_to='images/')


class vol_model(models.Model):
    
    first_name = models.CharField(max_length=30,
                                  validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                                             message='Please enter a valid name. Names may only contain alphabets.', 
                                                             code='invalid')])
    
    last_name = models.CharField(max_length=30,
                                 validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                                            message='Please enter a valid name. Names may only contain alphabets.', 
                                                            code='invalid')])

    
    date_of_birth = models.DateField()
    
    gender = models.CharField(max_length=6)
    
    email = models.EmailField(validators=[validate_email])
    
    phone_number = models.CharField(max_length=15,
                                    validators=[RegexValidator(regex='^([0-9+\\s]{5,15})+$', 
                                                               message='Please enter a valid phone number. Phone numbers may only contain numbers', 
                                                               code='invalid_phonenumber')])
    
    address = models.CharField(max_length=100)
    
    city = models.CharField(max_length=20,
                            validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                                       message='Please enter a valid city. City names may only contain alphabets.', 
                                                       code='invalid_city')])
    
    country = models.CharField(max_length=20,
                               validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                                          message='Please enter a valid country. Country names may only contain alphabets.', 
                                                          code='invalid_country')])
    
    postal_code = models.CharField(max_length=15,
                                   validators=[RegexValidator(regex='^([0-9]{0,5})+$', 
                                                              message='Please enter a valid postal code. Postal code may only contain numbers', 
                                                              code='invalid_postalcode')])
    
    description = models.CharField(max_length=300,
                                   default="",
                                   validators=[RegexValidator(regex='^[a-zA-Z0-9\'":()&$%-_@+#*=.;,?!\s]*$', 
                                                              message='Only the following special characters are allowed: ,.?!;\'"', 
                                                              code='invalid_description')],
                                   blank=True)

    is_active = models.BooleanField(default=False)
    

class ideas_model(models.Model):
    
    first_name = models.CharField(max_length=30,
                                  validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                                             message='Please enter a valid name. Names may only contain alphabets.', 
                                                             code='invalid')])
    
    last_name = models.CharField(max_length=30,
                                 validators=[RegexValidator(regex='^[a-zA-Z]+$', 
                                                            message='Please enter a valid name. Names may only contain alphabets.', 
                                                            code='invalid')])
    
    email = models.EmailField(validators=[validate_email], primary_key=True)
    
    phone_number = models.CharField(max_length=15,
                                    validators=[RegexValidator(regex='^([0-9]{5,15})+$', 
                                                               message='Please enter a valid phone number. Phone numbers may only contain numbers', 
                                                               code='invalid_phonenumber')])
    
    feedback = models.CharField(max_length=300, 
                                default="",
                                validators=[RegexValidator(regex='^[a-zA-Z0-9\'":()&$%-_@+#*=.;,?!\s]*$', 
                                                           message='Only the following special characters are allowed: ,.?!;\'"', 
                                                           code='invalid_description')])
    
    thoughts = models.CharField(max_length=300, 
                                default="",
                                validators=[RegexValidator(regex='^[a-zA-Z0-9\'":()&$%-_@+#*=.;,?!\s]*$', 
                                                           message='Only the following special characters are allowed: ,.?!;\'"', 
                                                           code='invalid_description')])


class count_model(models.Model):
    field_name1 = models.CharField(max_length=25, primary_key=True)
    field_value1 = models.IntegerField()
    field_name2 = models.CharField(max_length=25)
    field_value2 = models.IntegerField()
    field_name3 = models.CharField(max_length=25)
    field_value3 = models.IntegerField()
    field_name4 = models.CharField(max_length=25)
    field_value4 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = "Counter Section"

    def __str__(self):
        return self.name
    
    def clean(self):
            """
            Throw ValidationError if you try to save more than one model instance
            """
            model = self.__class__
            if (model.objects.count() > 0 and
                    self.id != model.objects.get().id):
                raise ValidationError(
                    "Can only create 1 instance of %s." % model.__name__)


class donors_model(models.Model):
    donor_name = models.CharField(max_length=30, primary_key=True)
    donor_location = models.CharField(max_length=60)
    donor_quote = models.TextField(max_length=400)

    
    def __str__(self):
        return self.donor_name

    def clean(self):
            """
            Throw ValidationError if you try to save more than one model instance
            """
            model = self.__class__
            if (model.objects.count() > 5 and
                    self.id != model.objects.get().id):
                raise ValidationError(
                    "Can only create 5 instance of %s." % model.__name__)

    