from django.shortcuts import render, HttpResponse
from crm_application.models import Lead
# Create your views here.

def home_view(request):
    lead = Lead.objects.all()
    return render(request,template_name='base.html', context={'lead':lead})