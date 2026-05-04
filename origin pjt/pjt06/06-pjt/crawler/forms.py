from django import forms


class CompanySearchForm(forms.Form):
    company_name = forms.CharField(
        label="회사명",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "예: 삼성, 네이버, 카카오",
                "autocomplete": "off",
            }
        ),
    )
