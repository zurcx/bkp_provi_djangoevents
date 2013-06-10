# encoding: utf-8


from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse


def home(request):
	context = {
		'nome': u'Luiz Fábio',
		'email:': u'luizfabiodacruz@gmail.com',
	}
	return render(request, "home.html", context)

def contact(request):
	return render(request, "contact.html", {})

