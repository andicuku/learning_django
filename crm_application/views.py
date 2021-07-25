from django.shortcuts import render, redirect

from crm_application.forms import LeadForm
from crm_application.models import Agent, Lead


# Create your views here.

def home_view(request):
    lead = Lead.objects.all()
    return render(request, template_name='base.html', context={'lead': lead})


def specific(request, pk):
    lead = Lead.objects.get(pk=pk)
    return render(request, 'specific_lead.html', context={'lead': lead})


def lead_create(request):
    print()
    form = LeadForm()
    if request.method == 'POST':
        print("Receiving data")
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("Lead created")
            return  redirect('leads:index')
    context = {
        'form': form
    }
    return render(request, 'lead_create.html', context)
