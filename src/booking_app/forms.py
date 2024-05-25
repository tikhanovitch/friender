from django import forms


class HotelAddForm(forms.Form):
    name = forms.CharField(max_length=40)
    stars = forms.IntegerField()
