from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from .forms import EmailLoginForm
from .forms import UserCreationForm
from django.urls import reverse

User = get_user_model()

class EmailLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'users/login.html'

@login_required
def member_list(request):
    # ログインユーザーの所属チームのメンバー一覧を取得
    if not hasattr(request.user, 'team'):
        return HttpResponseForbidden("あなたはまだチームに所属していません。")
    
    members = User.objects.filter(team=request.user.team)
    return render(request, 'users/member_list.html', {'members': members})

# メンバー詳細
@login_required
def member_detail(request, user_id):
    member = get_object_or_404(User, id=user_id)
    return render(request, 'users/member_detail.html', {'member': member})

# メンバー登録
@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True, team=request.user.team)  # ログインユーザーのチームを設定
            return redirect(reverse('member_list'))
    else:
        form = UserCreationForm()
    return render(request, 'users/create_user.html', {'form': form})