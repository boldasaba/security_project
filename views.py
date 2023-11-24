from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

from django.contrib import messages

from officer.forms import OfficerForm
from officer.forms import ClientForm
from officer.forms import DeploymentForm
from officer.forms import ClientPaymentForm

from officer.models import Officer
from officer.models import Client
from officer.models import Deployment
from officer.models import ClientPayment



# Create your views here.


def index_view(request):
    return render(request,'index.html' )


def officer_view(request):
    return render(request,'officer.html' )


def clients_view(request):
    return render(request, 'clients.html')


def deployment_view(request):
    return render(request, 'deployment.html' )


def login_view(request):
    return render(request, 'login.html')

@login_required
def add_officer_view(request):
    message = ''
    if request.method == "POST":
        officer_form = OfficerForm(request.POST,request.FILES)

        if officer_form.is_valid():
            officer_form.save()

            messages.success(request, "Information Added Successfully")
        

             
    officer_form = OfficerForm()

    officers = Officer.objects.all()    

    
    context = {

        'form': officer_form,
        'officers': officers,
        'msg':message
    }
    
    return render(request, "add_officer.html",context)

def edit_officer_view(request, officer_id):
    message = ''
    officer= Officer.objects.get(id=officer_id)
    if request.method == "POST":
        officer_form = OfficerForm(request.POST,request.FILES,instance=officer)
        if officer_form.is_valid():
            officer_form.save()
            message = "Changes have been made"

            return redirect(add_officer_view)

        else:
            message = "Invalid changes"

    else:
        officer_form = OfficerForm(instance=officer)

    context = {
        'form': officer_form,
        'officer': officer,
         'message':message,
    } 
    return render(request, 'edit_officer.html',context)

def delete_officer_view(request, officer_id):
    officer= Officer.objects.get(id=officer_id)
    officer.delete()

    return redirect(add_officer_view)




@login_required
def add_client_view(request):
    message = ''
    if request.method == "POST":
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            client_form.save()

            messages.success (request, "Information Added Successfully")
        else:
            message ="Invlid Information" 
    
    client_form = ClientForm()
        
    clients = Client.objects.all()     
    
    context = {

        'form': client_form,
        'msg':message,
        'clients': clients
        
    }


    return render(request, "add_client.html",context)

    
def edit_client_view(request, client_id):
    message = ''
    client= Client.objects.get(id=client_id)
    if request.method == "POST":
        client_form = ClientForm(request.POST,instance=client)
        if client_form.is_valid():
            client_form.save()
            message = "Changes have been made"
            return redirect(add_client_view)

        else:
            message = "Invalid changes"

    else:
        client_form = ClientForm(instance=client)

    context = {
        'form': client_form,
        'officer': client,
        'message':message,
    } 
    return render(request, 'edit_client.html',context)
    

def delete_client_view(request, client_id):
    client= Client.objects.get(id=client_id)
    client.delete()

    return redirect(add_client_view)


@login_required
def add_deployment_view(request):
    message = ''
    if request.method == "POST":
        deployment_form = DeploymentForm(request.POST)

        if deployment_form.is_valid():
            deployment_form.save()
            messages.success(request, "Information Added Successfully")
        else:
            message = "Invlid Information" 

    
    deployment_form = DeploymentForm()
    deployments = Deployment.objects.all() 
    context = {

        'form': deployment_form,
        'deployments': deployments,
        'message':message
    }


    return render(request, "add_deployment.html",context)
def edit_deployment_view(request, deployment_id):
    message = ''
    deployment= Deployment.objects.get(id=deployment_id)
    if request.method == "POST":
        deployment_form = DeploymentForm(request.POST,instance=deployment)
        if deployment_form.is_valid():
            deployment_form.save()
            message = "Changes have been made"
            return redirect(add_deployment_view)

        else:
            message = "Invalid changes"

    else:
        deployment_form = DeploymentForm(instance=deployment)

    context = {
        'form': deployment_form,
        'officer': deployment,
        'message':message,
    } 
    return render(request, 'edit_deployment.html',context)    

def delete_deployment_view(request, deployment_id):
    deployment= Deployment.objects.get(id=deployment_id)
    deployment.delete()

    return redirect(add_deployment_view)

@login_required
def add_client_payment_view(request):
    message = ''
    if request.method == "POST":
        client_payment_form = ClientPaymentForm(request.POST)

        if client_payment_form.is_valid():
           client_payment_form.save()
           messages.success(request, "Information Added Successfully")
        else:
            message = "Invlid Information" 
    
    client_payment_form = ClientPaymentForm()
    client_payments = ClientPayment.objects.all() 
    context = {

        'form': client_payment_form,
        'client_payments': client_payments,
        'message':message
    }


    return render(request, "add_client_payment.html",context)
def edit_client_payment_view(request, client_payment_id):
    message = ''
    client_payment= ClientPayment.objects.get(id=client_payment_id)
    if request.method == "POST":
        client_payment_form = ClientPaymentForm(request.POST,instance=client_payment)
        if client_payment_form.is_valid():
            client_payment_form.save()
            message = "Changes have been made"
            return redirect(add_client_payment_view)
            
            
        else:
            message = "Invalid changes"

    else:
        client_payment_form = ClientPaymentForm(instance=client_payment)

    context = {
        'form': client_payment_form,
        'officer': client_payment,
        'message':message,
    } 
    return render(request, 'edit_client_payment.html',context)

def delete_client_payment_view(request, client_payment_id):
    client_payment = ClientPayment.objects.get(id=client_payment_id)
    client_payment.delete()

    return redirect(add_client_payment_view)


def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            message = 'User Successfully Sign up'
        else:
            message = 'Sign up Failed'  
    else:
        sign_up_form = UserCreationForm()

    context ={

        'form': sign_up_form
    }                
    return  render(request, 'registration/sign_up.html',context )





