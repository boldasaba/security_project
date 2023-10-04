from django.contrib import admin

# Register your models here.
from .models import Officer,Client,Deployment,ClientPayment
class OfficerAdmin(admin.ModelAdmin):
    list_display = ("name","address","gender","birth_date","contact","grade")
admin.site.register(Officer,OfficerAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name","contact","address")
admin.site.register(Client,ClientAdmin)


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ("deployment_date","client_id","Shift","Officer_id")
admin.site.register(Deployment,DeploymentAdmin)


