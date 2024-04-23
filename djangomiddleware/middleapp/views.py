from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    print("view1")
    return HttpResponse("hello world!!!")
def hello(request):
    print("view2")
    return HttpResponse("hello accepted!!!")
