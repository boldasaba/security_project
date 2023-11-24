from django.forms import ModelForm
from officer.models import Officer,Client,Deployment,ClientPayment

class OfficerForm(ModelForm):
    class Meta:
        model = Officer
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class DeploymentForm(ModelForm):
    class Meta:
        model = Deployment
        fields = '__all__'

class ClientPaymentForm(ModelForm):
    class Meta:
        model = ClientPayment
        fields = '__all__'
        
