from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/<str:entry_name>", views.make_entry, name="entry"), 
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("random/", views.random_entry, name="random"), 
    path("edit/<str:edit_name>", views.edit, name="edit_page"),
    path("save_edit/<str:entry_name>", views.save_edit, name="save_edit")
]
 