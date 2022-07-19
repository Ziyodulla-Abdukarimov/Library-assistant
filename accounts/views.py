from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login as authlogin, logout
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user != None:
            authlogin(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('superadmin'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff"))
            else:
                return HttpResponseRedirect(reverse("student_profile"))
        else:
            a = messages.error(request, "Invalid Login Details")
    return render(request, 'accounts/login.html')


def log_out(request):
    logout(request)
    return redirect('login')
