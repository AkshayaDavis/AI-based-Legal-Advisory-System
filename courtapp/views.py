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


def add_jury(request):
    if request.method == 'POST':
        form = JuryForm(request.POST)
        if form.is_valid():
            jury = form.save(commit=False)
            jury.court = request.user  # Or assign a specific Register instance as needed
            jury.save()
            messages.success(request, "Jury added successfully", extra_tags="success")
            return redirect('view_juries')
        else:
            messages.error(request, "Invalid form data", extra_tags="error")
    else:
        form = JuryForm()
    return render(request, 'add_jury.html', {'form': form})



def view_juries(request):
    juries=Jury.objects.all()
    return render(request,'view_juries.html',{'juries':juries})

def edit_jury(request,id):
    jury = get_object_or_404(Jury, id=id)
    if request.method == 'POST':
        form = JuryForm(request.POST, instance=jury)
        if form.is_valid():
            jury = form.save(commit=False)
            jury.court = request.user  # Or assign a specific Register instance as needed
            jury.save()
            messages.success(request, "Jury updated successfully", extra_tags="success")
            return redirect('view_juries')
        else:
            messages.error(request, "Invalid form data", extra_tags="error")
    else:
        form = JuryForm(instance=jury)
    return render(request, 'add_jury.html', {'form': form})

def delete_jury(request,id):
    jury = get_object_or_404(Jury, id=id)
    jury.delete()
    messages.success(request, "Jury deleted successfully", extra_tags="success")
    return redirect('view_juries')


def schedule_trial(request, id):
    trial = get_object_or_404(Trial, id=id)  # Fetch Trial, not Schedule

    if request.method == 'POST':
        form = ScheduleTrial(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.status = "Scheduled"
            schedule.save()
            messages.success(request, "Trial scheduled successfully")
            return redirect('view_trial')  # Redirect to trial listing page
        else:
            messages.error(request, "Invalid form data")

    else:
        form = ScheduleTrial()

    return render(request, 'schedule_trial.html', {'form': form, 'trial': trial})


def reject_schedule(request, id):
    schedule = get_object_or_404(Schedule, id=id)  # Fetch the schedule entry using ID

    if request.method == "POST":
        reason = request.POST.get("reason")  # Get the rejection reason from the form
        schedule.status = "Rejected"
        schedule.rejection_reason = reason  # Ensure this field exists in your model
        schedule.save()

        return redirect("view_schedule")  # Redirect to the schedule view page

    return render(request, "reject_schedule.html", {"schedule": schedule})
    

def view_trial_schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'view_trial_schedule.html', {'schedules': schedules})