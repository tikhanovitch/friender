from django import forms


class HotelForm (forms.Form):
    name = forms.CharField(max_length=40)
    stars = forms.IntegerField()
