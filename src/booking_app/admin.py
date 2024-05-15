from django.contrib import admin
from .models import (
    User, Person, HotelOwner,
    Profile, Hotel, BookInfo,
    HotelsComment, PersonComment,
    Hobby
)


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", "last_name", "age",
        "sex", "created_at", "updated_at",
    ]


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", "last_name", "age",
        "sex", "created_at", "updated_at",
    ]


class HotelOwnerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", "last_name", "age",
        "sex", "created_at", "updated_at",
    ]


class ProfileAdmin(admin.ModelAdmin):
    pass
    list_display = [
        "photo", "id_card_number",
        "serial", "person_id",
    ]


class HotelAdmin(admin.ModelAdmin):
    list_display = [
        "name", "address", "stars",
        "rating", "owners",
    ]


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["detail", "book_time", "persons"]


class HotelsCommentAdmin(admin.ModelAdmin):
    list_display = ["hotel_rating", "hotels", "persons"]


class PersonCommentAdmin(admin.ModelAdmin):
    list_display = ["person_rating", "hotels", "persons"]


class HobbyAdmin(admin.ModelAdmin):
    list_display = ["name", "detail"]


admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(HotelOwner, HotelOwnerAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HotelsComment, HotelsCommentAdmin)
admin.site.register(PersonComment, PersonCommentAdmin)
admin.site.register(Hobby, HobbyAdmin)
