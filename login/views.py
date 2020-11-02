from django.shortcuts import render

# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request,'login/index.html')
    return render(request,'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return render(request,'login/logout.html')
