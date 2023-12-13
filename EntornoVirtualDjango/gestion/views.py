from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        "user":"Jesus Eduardo",
        "lenguajes" : ["Python","Java","C#"]
    }
    return render(request,"index.html",data)

def register(request):
    data = {
        "titulo":"Register"
    }
    return render(request,"register.html")

def dashboard(request):
    data = {
        "titulo":"Dashboard"
    }
    return render(request,"dashboard.html")
