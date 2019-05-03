from django.urls import path, include

from . import views

urlpatterns = [
    path('kontakt/', views.contact, name='contact'),
    path('ved/blandat', views.blandat_lovtrad, name='blandat_lovtrad'),
    path('ved/bjork', views.bjorkved, name='bjorkved'),
    path('ved/bok', views.bokved, name='bokved'),
    path('ved/ask', views.askved, name='askved'),
    path('ved/ovrigt', views.ovrigt, name='ovrigt'),
]
