from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def edit(request):
    return render(request,'edit.html')