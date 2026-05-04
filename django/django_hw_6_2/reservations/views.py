from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# 1. 예약 목록 조회 (이게 없어서 에러 났었어요!)
def index(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/index.html', {'reservations': reservations})

# 2. 예약 생성 페이지 제공
def new(request):
    form = ReservationForm()
    return render(request, 'reservations/new.html', {'form': form})

# 3. 예약 생성 로직 처리
def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:index')
        
        # [중요] 데이터가 유효하지 않으면 (날짜 형식 등), 
        # 에러 정보를 담은 폼을 들고 다시 입력 페이지로 갑니다.
        return render(request, 'reservations/new.html', {'form': form})
    
    return redirect('reservations:new')