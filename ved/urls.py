from django.urls import path, include
from ved.views import Contact, MixedHardWood, BirchWood, BeechWood, AshWood, Other


urlpatterns = [
    path('kontakt/', Contact.as_view(), name='contact'),
    path('ved/blandat', MixedHardWood.as_view(), name='blandat_lovtrad'),
    path('ved/bjork', BirchWood.as_view(), name='bjorkved'),
    path('ved/bok', BeechWood.as_view(), name='bokved'),
    path('ved/ask', AshWood.as_view(), name='askved'),
    path('ved/ovrigt', Other.as_view(), name='ovrigt'),
]
