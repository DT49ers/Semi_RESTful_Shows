from django.urls import path
from . import views

urlpatterns = [
  path('', views.all_shows),
  path('shows/new', views.add_show),
  path('shows/create', views.create_show),
  path('update_show/<int:id>', views.update_show),
  path('shows/<int:id>', views.view_show),
  path('shows', views.all_shows),
  path('shows/<int:id>/edit', views.edit_show),
  path('shows/<int:id>/destroy', views.delete_show),
]