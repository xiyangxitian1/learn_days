from django.conf.urls import url
# from .views import  index
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'hello/$', views.hello, name="hello"),
    # url(r'^weather/([a-zA-Z]+)/([0-9]+)/$', views.weather, name="weather"),
    url(r'^weather/(?P<city>[a-zA-Z]+)/(?P<year>[0-9]+)/$', views.weather, name="weather"),
    url(r'^get_form_data/$', views.get_form_data),
    url(r'^get_json_data/$', views.get_json_data),
    url(r'^test_respnse/$', views.test_respnse),
    url(r'^my_redirect/$', views.my_redirect),
]
