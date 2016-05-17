from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.core.exceptions import ValidationError
# 95172a7324019870220fd4304684e07d
def validate_length(value,length=24):
    print len(str(value))
    if len(str(value)) != length:
        raise ValidationError('Debes elegir 3 opciones')
def validate_year(value,length =4):
    if len(str(value)) != length:
        print len(str(value))
        raise ValidationError('Year is Incorrect')
gen =(('M','Masculino'),('F','Femenino'),)
class address(models.Model):
    zip_code = models.CharField(max_length=5, verbose_name=u'Postal Code: ')
    street = models.CharField (max_length=50, verbose_name=u'Address ')
    inside = models.CharField (max_length=10, verbose_name=u'Inside Number ')
    outside = models.CharField (max_length=10, verbose_name=u'Outside Number ')
    city = models.CharField (max_length=30, verbose_name=u'City')
    state = models.CharField (max_length=30, verbose_name=u'State ')
    
    def __unicode__(self):
        return self.street + ' ' + self.zip_code
class smes(User):
    RFC = models.CharField(max_length=13, choices=gen,verbose_name=u'RFC: ')
    ciec = models.CharField(max_length=30, verbose_name=u'CIEC:')
    
    def __unicode__(self):
        return self.RFC 
class investor(User):
    name = models.CharField(max_length=30, verbose_name=u'Name')
    last_name = models.CharField(max_length=30, verbose_name=u'Last name')
    gender = models.CharField(max_length=1, choices=gen,verbose_name=u'Gender: ')
    
    birth_date = models.DateField(auto_now=False,verbose_name=u'Birth Date')

    number = models.CharField(max_length=10, verbose_name=u'Phone')
    phone_number = models.CharField(max_length=10, verbose_name=u'Cellphone', blank=True)

    RFC = models.CharField(max_length=13, choices=gen,verbose_name=u'RFC: ')
    CURP = models.CharField(max_length=18,choices=gen,verbose_name=u'CURP: ')
    direct = models.ForeignKey(address, blank=False, null=False)
    
    income = models.CharField(max_length=40, verbose_name=u'How do you obtain money?(own business,employee) ')
    investment = models.ManyToManyField(smes,through='invest')

    def __unicode__(self):
        return self.name + ' ' + self.last_name

class investment(models.Model):
    investor = models.ForeignKey(investor)
    smes = models.ForeignKey(smes)
    date_invested = models.DateField(auto_now=False)



