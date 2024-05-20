from django.contrib import admin
from .models import (
    User, Person, HotelOwner,
    Profile, Hotel, BookInfo,
    HotelsComment, PersonComment,
    Hobby, Room, Booking,
)

#  _____Inlines_____


class BookInfoInline(admin.TabularInline):
    model = BookInfo
    extra = 1


class HotelsCommentInLine(admin.TabularInline):
    model = HotelsComment


class HobbyInline(admin.TabularInline):
    model = Hobby.owners.through
    extra = 1  # количество отбражаемых пустых полей


class ProfileInline(admin.TabularInline):
    model = Profile


class PersonCommentInline(admin.TabularInline):
    model = PersonComment


class HotelInline(admin.TabularInline):
    model = Hotel


#  _____Actions_____
@admin.action(description="Mark selected Hotels rating '5 stars'")
def make_five_stars(modeladmin, request, queryset):
    queryset.update(stars=5)


#  _____Admins_____

class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", "last_name", "age",
        "sex", "created_at", "updated_at",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["age", "sex"],
            },
        ),
    ]
    list_filter = ["first_name", "last_name", "age", "sex"]
    list_per_page = 10
    search_fields = ["first_name", "last_name", "age"]
    list_editable = ["age"]
    inlines = [
        HobbyInline,
        ProfileInline,
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
    inlines = [
        HotelInline,
        ProfileInline,
    ]


class ProfileAdmin(admin.ModelAdmin):
    pass
    list_display = [
        "person_id", "photo",
        "serial", "id_card_number",
    ]


class HotelAdmin(admin.ModelAdmin):
    list_display = [
        "name", "address", "stars",
        "rating", "owners",
    ]
    inlines = [
        BookInfoInline,
        HotelsCommentInLine,
        PersonCommentInline,
    ]
    actions = [
        make_five_stars,
    ]


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["detail", "book_time", "persons"]


class HotelsCommentAdmin(admin.ModelAdmin):
    list_display = ["hotel_rating", "hotels", "persons"]


class PersonCommentAdmin(admin.ModelAdmin):
    list_display = ["person_rating", "hotels", "persons"]


class HobbyAdmin(admin.ModelAdmin):
    list_display = ["name", "detail"]


class RoomAdmin(admin.ModelAdmin):
    list_display = ["number", "is_booked"]


class BookingAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date"]


admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(HotelOwner, HotelOwnerAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HotelsComment, HotelsCommentAdmin)
admin.site.register(PersonComment, PersonCommentAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
