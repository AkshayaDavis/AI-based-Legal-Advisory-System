from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import *
from django.conf import settings
from django.core.mail import send_mail 
import secrets,string
from django.db.models import Q
from django.db.models import Min
from django.shortcuts import get_object_or_404



def add_law(request):
    if request.method == 'POST':
        form = LawForm(request.POST)
        if form.is_valid():
            law = form.save(commit=False)
            law.court = request.user  # Or assign a specific Register instance as needed
            law.save()
            messages.success(request, "Law added successfully", extra_tags="success")
            return redirect('view_laws')
        else:
            messages.error(request, "Invalid form data", extra_tags="error")
    else:
        form = LawForm()
    return render(request, 'add_law.html', {'form': form})


def view_laws(request):
    laws=Law.objects.all()
    return render(request,'view_laws.html',{'laws':laws})

def edit_law(request,id):
    law = get_object_or_404(Law, id=id)
    if request.method == 'POST':
        form = LawForm(request.POST, instance=law)
        if form.is_valid():
            law = form.save(commit=False)
            law.court = request.user  # Or assign a specific Register instance as needed
            law.save()
            messages.success(request, "Law updated successfully", extra_tags="success")
            return redirect('view_laws')
        else:
            messages.error(request, "Invalid form data", extra_tags="error")
    else:
        form = LawForm(instance=law)
    return render(request, 'add_law.html', {'form': form})

def delete_law(request,id):
    law = get_object_or_404(Law, id=id)
    law.delete()
    messages.success(request, "Law deleted successfully", extra_tags="success")
    return redirect('view_laws')
    