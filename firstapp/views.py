from django.shortcuts import render

# Create your views here.

def load_home_page(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def kerala(request):
    return render(request,'kerala.html')
def alappuzha(request):
    return render(request,'alappuzha.html')
def beypore(request):
    return render(request,'beypore.html')
def gavi(request):
    return render(request,'gavi.html')
def bekal(request):
    return render(request,'bekal.html')
