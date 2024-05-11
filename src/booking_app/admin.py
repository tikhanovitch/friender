from .models import (
    User, Person, HotelOwner,
    Profile, Hotel, BookInfo,
    HotelsComment, PersonComment,
    Hobby
)

from django.contrib import admin

admin.site.register(User)
admin.site.register(Person)
admin.site.register(HotelOwner)
admin.site.register(Profile)
admin.site.register(Hotel)
admin.site.register(BookInfo)
admin.site.register(HotelsComment)
admin.site.register(PersonComment)
admin.site.register(Hobby)
