# reservations/forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'  # 모든 필드를 제공한다는 요구사항 반영