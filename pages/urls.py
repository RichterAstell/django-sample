from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
    path('form', views.form, name='form'),
]
