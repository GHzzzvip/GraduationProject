from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            """
                index页加装饰器@login_required需要登陆才能查看
                调用auth_login(request, user)才能够访问index页面
            """
            auth_login(request, user)

            # 重定向页面
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


