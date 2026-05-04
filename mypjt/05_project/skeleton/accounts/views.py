from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from community.models import Post

# [F502] 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 가입 완료 시 자동 로그인
            return redirect('community:asset_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# [F503] 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('community:asset_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# [F504] 로그아웃
def logout(request):
    auth_logout(request)
    messages.success(request, '로그아웃되었습니다.')
    return redirect('community:asset_list')

# [F505] 비밀번호 변경
@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # 세션 무효화 방지
            messages.success(request, '비밀번호가 변경되었습니다.')
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/update_password.html', {'form': form})

# [F507] 프로필 페이지
@login_required
def profile(request):
    # 본인이 작성한 게시글을 username 기반으로 검색
    user_posts = Post.objects.filter(author=request.user.username).order_by('-created_at')
    
    # 쉼표로 구분된 관심 종목을 리스트로 변환하여 템플릿에 전달
    interests = []
    if request.user.interest_stocks:
        interests = [stock.strip() for stock in request.user.interest_stocks.split(',')]
        
    context = {
        'user_posts': user_posts,
        'interests': interests,
    }
    return render(request, 'accounts/profile.html', context)