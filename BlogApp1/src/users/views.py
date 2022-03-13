from django.shortcuts import render, redirect
from .forms import RegisterationForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    form = RegisterationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('login')  login page imiz henüz yok.
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/register.html', context )

def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect(request.path)
    
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    
    return render(request, "users/profile.html", context)