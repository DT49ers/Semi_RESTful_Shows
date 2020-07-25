from django.db import models
# Create your models here.

class ShowManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    # add keys and values to errors dictionary for each invalid field
    if len(postData['title']) < 2:
      errors["title"] = "Show title must be at least 2 characters"
    if len(postData['network']) < 3:
      errors["network"] = "Show network must be at least 3 characters"
    if len(postData['description']) < 10:
      errors["description"] = "Show description must be at least 10 characters"
    if len(postData['release_date']) == 0:
      errors["release_date"] = "Release Date must not be left empty"
    return errors

class Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=45)
  release_date = models.DateField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()

