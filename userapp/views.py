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


def index(request):
    if request.session.get('ut') == 'user':
        lawyers = Register.objects.filter(usertype="lawyer")
        return render(request, 'index.html', {'lawyers': lawyers})
    else:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def reg(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        
        if form.is_valid():
            email=form.cleaned_data['email']
            data=Register.objects.filter(email=email).first()
            if data:
                messages.error(request,"Email already exists",extra_tags="error")
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="user"
                user.password=make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"Registration Successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"Registration failed",extra_tags="error")
            form=RegisterForm()
            return render(request,'reg.html',{'form':form,'title':'User Registration','button':'Register'})
    else:
        form=RegisterForm()
    return render(request, 'reg.html',{'form':form,'title':'User Registration','button':'Register'})

def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                users=Register.objects.get(username=user)
                request.session['ut']=users.usertype
                request.session['uid']=users.id 
                request.session['uname']=users.username
                messages.success(request,"Login Successfull",extra_tags="success")
                return redirect('/')
            else:
                messages.error(request,"Invalid Username and Password",extra_tags="error")
        else:
            messages.error(request,"Login Failed",extra_tags="error")
            form=LoginForm()
            return render(request,'user_login.html',{'form':form})
    else:
        form=LoginForm()
    return render(request, 'user_login.html',{'form':form})

def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    messages.success(request,"Logout Successfull",extra_tags="success")
    return redirect('/')

def view_user(request):
    users=Register.objects.filter(usertype="user")
    return render(request,'users.html',{'users':users})

def profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request, 'profile.html',{'user':user})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'reg.html', {'form': form,'title':'Edit Profile','button':'Update'})

def forgot_password(request):
    if request.method=='POST':
        form=ForgotPasswordForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            data=Register.objects.filter(email=email)
            if data:
                new_password=generate_random_password()
                user=Register.objects.get(email=email)
                Reset.objects.create(otp=new_password,user=user)
                subject="Reset Password "
                message=f'Your one time password is {new_password}'
                email_from=settings.EMAIL_HOST_USER
                email_to=[email]
                send_mail(subject,message,email_from,email_to)
                messages.success(request,"E-mail has been send",extra_tags="success")
                return redirect('reset_password')
            else:
                messages.error(request, "Invalid E-mail", extra_tags="error")
        else:
            messages.error(request, "Invalid form", extra_tags="error")
    else:
        form=ForgotPasswordForm()
    return render(request,'forgot_password.html',{'form':form})

def generate_random_password(length=6):
    characters=string.ascii_letters+string.digits
    password=''.join(secrets.choice(characters) for _ in range(length))
    return password

def reset_password(request):
    if request.method == 'POST':
        form=ResetPasswordForm(request.POST)
        if form.is_valid():
            otp=form.cleaned_data['otp']
            email=form.cleaned_data['email']
            user = Register.objects.get(email=email)
            user_otp=Reset.objects.filter(user=user).first()
            if user_otp.otp == otp:
                newpassword=form.cleaned_data['newpassword']
                data=Register.objects.get(id=user.id)
                data.password=make_password(newpassword)
                data.save()

                user_otp.delete()

                messages.success(request,"Password changed", extra_tags="success")
                return redirect('user_login')
            else:
                messages.error(request,"Inavalid otp", extra_tags="error")
        else:
            messages.error(request,"Inavalid form data", extra_tags="error")
    else:
        form=ResetPasswordForm()
    return render(request,'reset_password.html',{'form':form})

def delete_user(request,id):
    user=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'user deleted successfully',extra_tags='success')
    return redirect('view_user')

def lawyer_reg(request):
    if request.method == 'POST':
        form=LawyerRegisterForm(request.POST)
        
        if form.is_valid():
            email=form.cleaned_data['email']
            data=Register.objects.filter(email=email).first()
            if data:
                messages.error(request,"Email already exists",extra_tags="error")
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="lawyer"
                user.password=make_password(form.cleaned_data['password'])
                user.save()
                subject="Account Deletion Notification"
                message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
                email_from=settings.EMAIL_HOST_USER
                email_to=[user.email]
                send_mail(subject, message, email_from, email_to)
                messages.success(request,"Registration Successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"Registration failed",extra_tags="error")
            form=LawyerRegisterForm()
            return render(request,'lawyer_reg.html',{'form':form,'title':'Register','button':'Register'})
    else:
        form=LawyerRegisterForm()
    return render(request, 'lawyer_reg.html',{'form':form,'title':'Lawyer Registration','button':'Register'})

def lawyer_profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request, 'lawyer_profile.html',{'user':user})

def edit_lawyer_profile(request):
    if request.method == 'POST':
        form = EditLawyerProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('lawyer_profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = EditLawyerProfileForm(instance=request.user)

    return render(request, 'lawyer_reg.html', {'form': form,'title':'Edit Profile','button':'Update'})

def reg_option(request):
    return render(request,'reg_option.html')

def view_lawyer(request):
    users=Register.objects.filter(usertype="lawyer")
    return render(request,'lawyers.html',{'users':users})

def delete_lawyer(request,id):
    user=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {user.first_name} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)
    user.delete()
    messages.success(request,'Lawyer deleted successfully',extra_tags='success')
    return redirect('view_lawyer')

def court_reg(request):
    if request.method == 'POST':
        form=CourtRegisterForm(request.POST)
        
        if form.is_valid():
            email=form.cleaned_data['email']
            data=Register.objects.filter(email=email).first()
            if data:
                messages.error(request,"Email already exists",extra_tags="error")
                return redirect('view_court')
            else:
                user=form.save(commit=False)
                user.usertype="court"
                user.password=make_password(form.cleaned_data['password'])
                user.save()
                subject="Account Activation Notification"
                message=f"Dear {user.username} Your account is being created. Your username is {user.username} and password is {user.password}. Please login and change your password for security reasons..."
                email_from=settings.EMAIL_HOST_USER
                email_to=[user.email]
                send_mail(subject, message, email_from, email_to)
                messages.success(request,"Registration Successfull",extra_tags="success")
                return redirect('view_court')
        else:
            messages.error(request,"Registration failed",extra_tags="error")
            form=CourtRegisterForm()
            return render(request,'court_reg.html',{'form':form,'title':'Court Registration','button':'Register'})
    else:
        form=CourtRegisterForm()
    return render(request, 'court_reg.html',{'form':form,'title':'Court Registration','button':'Register'})

def view_court(request):
    users=Register.objects.filter(usertype="court")
    return render(request,'courts.html',{'users':users})

def delete_court(request,id):
    user=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'court deleted successfully',extra_tags='success')
    return redirect('view_court')


def lawyer_profileview(request):
    query = request.GET.get('q', '')  # Get search query
    lawyers = Register.objects.filter(usertype="lawyer")  # Filter only lawyers

    if query:
        # Apply search filters
        lawyers = lawyers.filter(
            Q(first_name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(qualification__icontains=query) |
            Q(username__icontains=query)
        )
    else:
        # Select one lawyer per specialization (minimum ID per specialization)
        specializations = Register.objects.filter(usertype="lawyer").values('specialization').annotate(min_id=Min('id'))
        lawyer_ids = [entry['min_id'] for entry in specializations]
        lawyers = Register.objects.filter(id__in=lawyer_ids)

    return render(request, 'lawyer_profileview.html', {'lawyers': lawyers})



def all_lawyers(request):
    lawyers = Register.objects.filter(usertype="lawyer") 
    return render(request, 'all_lawyers.html', {'lawyers': lawyers})



def court_profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request, 'court_profile.html',{'user':user})

def edit_court_profile(request):
    if request.method == 'POST':
        form = EditCourtProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('court_profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = EditCourtProfileForm(instance=request.user)

    return render(request, 'court_reg.html', {'form': form,'title':'Edit Profile','button':'Update'})
