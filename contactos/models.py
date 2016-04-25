from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'Actividad')
    description = models.CharField(max_length=120, verbose_name=u'Description')

    def __unicode__(self):
        return self.name 

class Person(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'Nombre')
    last_name = models.CharField(
        max_length=120, blank=True, null=True, verbose_name=u'Apellido'
    )
    number = models.CharField(max_length=10, verbose_name=u'Numero')
    phone_number = models.CharField(
        max_length=10, verbose_name=u'Celular', blank=True
    )
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User)

    likes = models.ManyToManyField(Activity)

    def __unicode__(self):
        return self.name + ' ' + self.last_name

class Group(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'Nombre')
    description = models.CharField(max_length=300, verbose_name=u'Descripcion')
    person = models.ManyToManyField(Person)
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity, blank=False, null=False)

    def __unicode__(self):
        return self.name
