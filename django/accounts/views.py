from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.models import CustomUser
from accounts.forms import AuthForm

# ユーザー認証
def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # ユーザー認証
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            request.session['pk'] = user.pk
            login(request, user)
            return redirect('top')
        messages.error(request, "ユーザIDまたはパスワードが正しくありません。")
    
    # getパラメータで受け取ったnextをtemplateへ渡す
    redirect_to = request.GET.get('next')
    
    return render(request, 'accounts/auth.html', {'form': form, 'redirect_to': redirect_to})


def loguout_view(request):
    logout(request)
    request.session.clear()
    return redirect('login')
