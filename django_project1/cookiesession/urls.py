from django.conf.urls import url
# from .views import  index
from . import views

urlpatterns = [
    url(r'^cookie_demo/?$', views.cookie_demo, name="cookie_demo"),
    url(r'^session_demo/?$', views.session_demo, name="session_demo"),
]
