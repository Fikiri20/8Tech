from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from .mailing import send_registration_email
from .forms import ResetPasswordEmailCollection, PasswordResetForm

# Create your views here.

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('accounts:login')
        
    else:
        return render(request,'login.html')

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()

                context = {
                    "username": username,
                    "link": "8tech.pythonanywhere.html"
                }

                send_registration_email(to=email, subject="Account Creation", context=context)
                print('user created')
                return redirect('accounts:login')
        
        else:
            messages.info(request,'password not matching..')
            return redirect('accounts:register')
        # return redirect('/') this line is null as it does nothing
        
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def password_reset_request(request):
    if request.method == 'POST':
        form = ResetPasswordEmailCollection(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_user = User.objects.filter(email=email).first()
            if associated_user:
                subject = "Password Reset Requested"
                email_template_name = "password_reset_email.html"
                context = {
                    "email": associated_user.email,
                    "domain": request.META['HTTP_HOST'],
                    "site_name": "8Tech Solutions",
                    "uid": urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    "user": associated_user,
                    "token": default_token_generator.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http',
                }
                email = render_to_string(email_template_name, context)
                send_mail(subject, email, '8teqsolution@gmail.com', [associated_user.email], fail_silently=False)
            return redirect("accounts:password_reset_done")
    else:
        form = ResetPasswordEmailCollection()
    return render(request, "password_reset_form.html", {"form": form})


def password_reset_confirm(request, uidb64=None, token=None):
    if uidb64 is not None and token is not None:
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = PasswordResetForm(request.POST)
                if form.is_valid():
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']
                    if password1 == password2:
                        user.set_password(password1)
                        user.save()
                        update_session_auth_hash(request, user)  # Important for keeping the user logged in
                        return redirect('accounts:password_reset_complete')
                    else:
                        form.add_error('password2', "Passwords do not match.")
            else:
                form = PasswordResetForm()
            return render(request, 'password_reset_confirm.html', {'form': form})
        else:
            # Invalid link, show error or redirect
            return redirect('accounts:password_reset_invalid')
    else:
        # No uid or token, show error or redirect
        return redirect('accounts:password_reset_invalid')
    


def password_reset_done(request):
    return render(request, 'password_reset_done.html')

from django.shortcuts import render

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')



