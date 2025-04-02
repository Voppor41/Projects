from django.contrib import admin
from .models import Users, News, Match, Players


# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("date", "op_team")

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ("nickname", "statistic")