from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    my_dict = {
    #   'insert_something':"Calc app",
      'name':'Akira',
      'first': 0,
      'second': 0,
    }
    return render(request,'polls/index.html', my_dict)