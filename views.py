from django.shortcuts import render

# Create your views here.
def officer_view(request):
    return render(request,'officer.html' )


def clients_view(request):
    return render(request, 'clients.html')

def deployment_view(request):
    return render(request, 'deployment.html' )

def login_view(request):
    return render(request, 'login.html')



