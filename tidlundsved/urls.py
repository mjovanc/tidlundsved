from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from tidlundsved.views import IndexPageView, AboutPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('om-oss/', AboutPageView.as_view(), name='about'),
    path('', include('ved.urls')),
]
