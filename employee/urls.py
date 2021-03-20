from django.urls import path

from . import views

app_name = 'employee'
urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('', views.index, name='search'),
]
