from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Developer

# Create your views here.





def home(request):
    developer = Developer.objects.get(id=1)
    skills = developer.skills.all()
    for s in skills:
        print(s)

    context = {'name': developer.name, 
               'profile_name' : developer.profile_name, 
               'career_objective' : developer.career_objective,
               'skills': skills}
    return render(request, 'home.html', context)
