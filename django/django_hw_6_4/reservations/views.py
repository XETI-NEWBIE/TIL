from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# 1. 예약 목록 조회
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

# [요구사항] new 함수는 삭제! 
# [요구사항] create 함수 안에서 GET과 POST 분기 처리
def create(request):
    # 1. POST 요청일 때 (사용자가 '예약 생성' 버튼을 눌렀을 때)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:index')
            
    # 2. GET 요청일 때 (처음 '예약 하기'를 눌러서 빈 화면을 보고 싶을 때 - 기존 new 역할)
    else:
        form = ReservationForm()
    
    # POST에서 유효성 검사가 실패했거나, GET 요청으로 처음 들어왔을 때 모두 여기로 옵니다.
    context = {
        'form': form
    }
    # [요구사항] new.html 대신 create.html을 렌더링
    return render(request, 'reservations/create.html', context)