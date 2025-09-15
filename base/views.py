from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'base/home.html', {})
#Work Section
def about_page(request):
    return render(request, 'base/about.html', {})

def about_technologies_page(request):
    return render(request, 'base/about_technologies.html', {})

def about_dev_page(request):
    return render(request, 'base/about_development.html', {})


def work_page(request):
    return render(request, 'base/work.html', {})

def projects_page(request):
    return render(request, 'base/projects.html', {})

def contact_page(request):
    return render(request, 'base/contact.html', {})


