from django.urls import path

from . import views
app_name = 'wiki'

urlpatterns = [
    path("random_page/", views.random_page, name="random_page"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("new/", views.new, name="new"),
    path("search", views.search, name="search"),
    path('wiki/<str:title>', views.entry, name="entry"),
    path("", views.index, name="index"),

]
