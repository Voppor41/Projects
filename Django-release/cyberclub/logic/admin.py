from django.contrib import admin
from .models import Users, News, Match

# Register your models here.
admin.site.register(Users)
admin.site.register(News)
admin.site.register(Match)