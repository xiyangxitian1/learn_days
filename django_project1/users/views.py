from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import json


# Create your views here.

def my_redirect(request):
    print(reverse(hello))
    return redirect(reverse(hello))

def index(request):
    return HttpResponse("Hello World")


def hello(request):
    return HttpResponse("Hello 啊")


def weather(request, year, city):
    result = city + year
    # result = "weather"
    query_dict = request.GET
    a = query_dict.get('a')
    result += a
    return HttpResponse(result)


def test_respnse(request):
    # return HttpResponse(content='itcast python', status=400)
    # 或者下面这种写法
    response = HttpResponse('itcast python')
    response.status_code = 400
    response['Itcast'] = 'Python'  # 会在响应头里
    return response


# 获取请求体中的非表单数据 request.body  POST请求
def get_json_data(request):
    data_bytes = request.body  # bytes类型的数据
    print(data_bytes, type(data_bytes))
    data_str = data_bytes.decode()
    # data = json.dumps(data_str, ensure_ascii=False)  #  dumps是转成字符串
    data = json.loads(data_str)
    print(data, type(data))
    return HttpResponse(data)


def get_form_data(request):
    print(request.POST)
    query_dict = request.POST
    print("query_dict", query_dict)
    # query_dict.dict()  转成普通字典
    name = query_dict.get('name')
    return HttpResponse(name)
