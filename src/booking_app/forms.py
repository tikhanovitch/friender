from django import forms

from .models import Hotel, User


# class HotelAddForm (forms.Form):
#     name = forms.CharField(max_length=40)
#     stars = forms.IntegerField()(validator=[validate_hotel_stars])

class HotelModelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "stars", "address", "description", "photo"]
        widgets = {
            "description": forms.Textarea(attrs={"size": 100, 'class': 'special', "required": False})
        }


class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "age", "sex"]
