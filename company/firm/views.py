from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *


def employee_create(request):
	form = EmployeeForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	context = {
		"form": form,
	}
	return render(request, "employee_form.html", context)


def employee_detail(request, slug=None):
	instance = get_object_or_404(Employees, slug=slug)
	context = {
		"instance": instance,
		"title": instance.title,
	}
	return render(request, "employee_detail.html", context)


def employee_list(request):
	queryset_list = Employees.objects.all()

	context = {
		"queryset_list": queryset_list,
	}
	return render(request, "employee_list.html", context)


def employee_update(request, slug=None):
	instance = get_object_or_404(Employess, slug=slug)
	form = EmployeeForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "employee_form.html", context)