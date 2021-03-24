from django.urls import path

from . import views

app_name = 'employee'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('login/', views.Login.as_view(), name='login'),
    # path('', views.index, name='search'),
]
