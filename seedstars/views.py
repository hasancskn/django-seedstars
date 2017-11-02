from django.http import *
from models import Person
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .forms import PersonForm

def listPage(req):
	return render(req, "list.html", {"data": Person.objects.all()})

def createPage(req):
	if req.method == 'GET':
		return render(req, "create.html", {})
	else:
		form = PersonForm(req.POST)
		if form.is_valid():
			p = Person(name=form.cleaned_data["name"], email=form.cleaned_data["email"])
			p.save()
			return HttpResponseRedirect("list")
		else:
			return render(req, "create.html", {'form': form})

def homePage(req):
	return render(req, "home.html", {})