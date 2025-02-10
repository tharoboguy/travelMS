from django.urls import path
from . import views

urlpatterns = [
path('homepage',views.index, name='homepage'),
path('destination', views.destin, name='destination'),
path('about', views.about, name='about'),
path('contact', views.contact, name='contact'),
path('booking', views.booking, name='booking'),
path('logout', views.logout, name='logout')
]