from django.shortcuts import render

# Create your views here.
from django import http


def cookie_demo(request):
    response = http.HttpResponse('cookie_demo')
    response.set_cookie(key='name', value='cg', max_age=None)
    response.set_cookie(key='name1', value='cg1', max_age=None)
    response.set_cookie(key='name2', value='cg2', max_age=None)
    name = request.COOKIES.get('name')
    name1 = request.COOKIES.get('name1')
    name2 = request.COOKIES.get('name2')
    print(name)
    print(name1)
    print(name2)
    return response


def session_demo(request):
    # request.session['session_mykey9'] = 'lc'
    return http.HttpResponse(request.session.get("session_mykey9", 78))
