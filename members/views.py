from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberRegistrationForm

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = MemberRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')

# Create your views here.
