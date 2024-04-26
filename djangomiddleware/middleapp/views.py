from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("Process Start")

def hello(request):
    print("yes")
    return HttpResponse("hello world!!!")

def viewlogs(request):
    with open('C:/Users/SANJEEV/Documents/GitHub/my project/djangomiddleware/djangomiddleware/logfile.log', 'r') as log_file:
        log_content = log_file.read()
    return HttpResponse(log_content, content_type='text/plain')

def auth(request):
    return HttpResponse("auth succesfull")