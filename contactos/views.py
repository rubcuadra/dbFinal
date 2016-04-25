from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from .models import Person, Group
from django.views.generic import View 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms as cForms


class PersonView(View):
    template_name = 'person.html'
    def get(self, request):
        form = cForms.PersonForm()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = cForms.PersonForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('/contactos/')
        else:
            return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(PersonView, self).dispatch(request, *args, **kwargs)

class GroupView(View):
    template_name = "formgrups.html"
    def get(self, request):
        form = cForms.GroupForm(usuario = request.user)
        return render(request, self.template_name, locals())

    def post(self, request):
        print 'dddd'
        print request.user
        form = cForms.GroupForm(request.POST, usuario=request.user)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('/grupos/')
        else:
            return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(GroupView, self).dispatch(request, *args, **kwargs)

def home(request):
    return render(
        request,
        'index.html',
        {}
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(
        request, 'register.html', {'form': form}
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('get_contactos'))
        else:
            return redirect(reverse('login'))
    else:
        form = AuthenticationForm()
        return render(
            request,
            'login.html',
            {'form': form}
        )


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

@login_required
def get_contactos(request):
    user = request.user
    contactos = Person.objects.filter(user=user)

    return render(
        request,
        'contactos.html',
        {'contactos': contactos}
    )

@login_required
def edit_contactos(request, primaryKey):
    user = request.user
    instan = Person.objects.get(pk = primaryKey)
    contactpK = primaryKey   
    if request.method == 'POST': 
        form = cForms.PersonForm(request.POST, instance = instan)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('/contactos/')
        else:
            return render(request,'editContactos.html',locals())
    elif request.method == 'GET':
        form = cForms.PersonForm(instance = instan)
        return render(
            request,
            'editContactos.html',
            {'locals':locals()}
        )
@login_required
def edit_grupos(request, primaryKey):
    user = request.user
    instan = Group.objects.get(pk = primaryKey)
    grouppK = primaryKey   

    if request.method == 'POST':       
        form = cForms.GroupForm(request.POST, instance = instan)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('/grupos/')
        else:
            return render(request,'editGrupos.html',locals())
    elif request.method == 'GET':
        form = cForms.GroupForm(instance = instan)
        return render(
            request,
            'editGrupos.html',
            {'locals':locals()}
        )

@login_required
def get_grupos(request):
    user = request.user
    grupos = Group.objects.filter(user=user)
    return render(
        request,
        'grupos.html',
        {'grupos': grupos}
    )
@login_required
def delete_contact(request, primaryKey):
    cont = Person.objects.get(pk = primaryKey)
    print "Si corre", cont
    cont.delete()
    return redirect(reverse("get_contactos")) 

@login_required
def delete_group(request, primaryKey):
    cont = Group.objects.get(pk = primaryKey)
    cont.delete()
    return redirect(reverse("get_grupos")) 



