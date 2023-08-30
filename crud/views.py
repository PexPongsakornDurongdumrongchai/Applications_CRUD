from django.shortcuts import render, redirect
from .models import Member
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
#@login_required
def index(request):
    return render(request, 'index.html')


#@login_required
def list(request):
    members_list = Member.objects.all()
    paginator = Paginator(members_list, 5)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'members': members})

#@login_required
def create(request):
    if request.method == 'POST':
        member = Member(
            companyname=request.POST['companyname'],
            fullname=request.POST['fullname'],
            jobtitle=request.POST['jobtitle'],
            emailaddress=request.POST['emailaddress'],
            softwareusername=request.POST['softwareusername'],
            expirationdate=request.POST['expirationdate'],
            version=request.POST['version'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Software was created successfully!')
        return redirect('/list')
    else:
        return render(request, 'add.html')

#@login_required
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)


#@login_required
def update(request, id):
    member = Member.objects.get(id=id)
    member.companyname = request.POST['companyname']
    member.fullname = request.POST['fullname']
    member.jobtitle = request.POST['jobtitle']
    member.emailaddress = request.POST['emailaddress']
    member.softwareusername = request.POST['softwareusername']
    member.expirationdate = request.POST['expirationdate']
    member.version = request.POST['version']
    
    member.save()
    messages.success(request, 'Software was updated successfully!')
    return redirect('/list')

#@login_required
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.warning(request, 'Software was deleted successfully!')
    return redirect('/list')


#@login_required
def view(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'view.html', context)