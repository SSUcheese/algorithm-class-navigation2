from dataclasses import field, fields
from django import forms
from .models import Route

class GetRoute(forms.ModelForm):
    class Meta:
        model = Route
        fields= [
            "question",
            "start_point",
            "end_point",
            "route"
        ]
        widgets = {
            "question": forms.RadioSelect, # 이렇게 하면 기본값으로 사용되는 select 대신에 radioselect 위젯이 사용된다.
            "route": forms.RadioSelect, # 이렇게 하면 기본값으로 사용되는 select 대신에 radioselect 위젯이 사용된다.
        }