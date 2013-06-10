# encoding: utf-8

from django import forms

from django.core.mail import send_mail

class ContactForm(forms.Form):

	name = forms.CharField(label=u'Nome')
	email = forms.EmailField(label=u'E-mail')
	message = forms.CharField(label=u'Mensagem',
							  widget=forms.Textarea)
	def send_mail(self):
		subject = u'E-mail de Contado de: %s' % self.cleaned_data['name']
		message = u'E-mail: %s\n Mensagem: %s' %\
					(self.cleaned_data['email'], self.cleaned_data['message'])
		send_mail(subject, message, 'luizfabiodabruz@gmail.com',
			['luizfabiodacruz@gmai.com'])