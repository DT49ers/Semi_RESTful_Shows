from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

# Create your views here.

from shows_app.models import *
def index(request):
  return render(request, 'index.html')

def add_show(request):

  return render(request, 'add_show.html')

def create_show(request):
  print(request.POST)
  # check that all form fields pass the validations
  errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
  if len(errors) > 0:
      # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
    for key, value in errors.items():
      messages.error(request, value)
      # redirect the user back to the form to fix the errors
    return redirect('/shows/new')
  else:
    # add show that was created in the db
    # redirect to the display_show template
    show = Show.objects.create(
      title = request.POST['title'],
      network = request.POST['network'],
      release_date = request.POST['release_date'],
      desc = request.POST['description'],
      )
    return redirect(f'/shows/{ show.id }')

def view_show(request, id):
  context = {

    "show" : Show.objects.get(id=id)
  }
  
  return render(request, 'display_show.html', context)

def all_shows(request):

  context = {
    
    'shows' : Show.objects.all()
  }
  
  return render(request, 'all_shows.html', context)

def update_show(request, id):
  print(request.POST)
  show = Show.objects.get(id=id)
  # check that all form fields pass the validations
  errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
  if len(errors) > 0:
      # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
    for key, value in errors.items():
      messages.error(request, value)
      # redirect the user back to the form to fix the errors
    return redirect(f'/shows/{show.id}/edit')
  else:
    update_show = Show.objects.get(id=id)
    update_show.title = request.POST['title']
    update_show.network = request.POST['network']
    update_show.release_date = request.POST['release_date']
    update_show.desc = request.POST['description']
    update_show.save()
  return redirect(f'/shows/{update_show.id}')

def edit_show(request, id):

  context = { 
    'show' : Show.objects.get(id=id)
  }

  return render(request, 'edit_show.html', context)

def delete_show(request, id):
  delete_show = Show.objects.get(id=id)
  delete_show.delete()

  return redirect('/shows')