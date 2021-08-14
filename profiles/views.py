from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account for {username} is created")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'profiles/register.html',{'form' : form})