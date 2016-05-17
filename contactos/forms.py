from django import forms
'''from .models import Person ,Group

class PersonForm(forms.ModelForm):

	def save(self, user, *args, **kwargs):
		self.instance.user = user
		super(PersonForm, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		widgets = {'likes': forms.CheckboxSelectMultiple}
		# fields
class GroupForm(forms.ModelForm):
	def save(self,user,*args,**kwargs):
		self.instance.user = user
		super(GroupForm, self).save(*args, **kwargs)
		#select column_name from information_schema.columns where table_name = 'contactos_person';
	def __init__(self, *args, **kwargs):
		#Si vamos a Crear Nuevo, Edit nos da Instance
		user = kwargs.pop('usuario') if 'usuario' in kwargs else kwargs.pop('instance').user
		super(GroupForm, self).__init__(*args, **kwargs)
		self.fields['person'].queryset = Person.objects.filter(user = user)
			
		
	class Meta:
		model = Group
		exclude = ('user', )
		widgets = {'person': forms.CheckboxSelectMultiple}
'''