from django.shortcuts import render

# Create your views here.
def place1(request):
    return render(request,'place1.html')
def place2(request):
    return render(request,'place2.html')