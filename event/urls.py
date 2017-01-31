from django.conf.urls import url
from event import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name="register"),
    url(r'^contact/$', views.contact, name="contact"),
]
