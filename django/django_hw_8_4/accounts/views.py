from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

# 1. 전체 유저 목록 조회
def index(request):
    User = get_user_model()  # 활성화된 커스텀 유저 모델 가져오기
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)

# 2. 로그인 기능
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 검사를 통과하면 로그인 처리
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        # GET 요청일 때는 빈 폼을 보여줌
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 3. 로그아웃 기능
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('accounts:index')