from django.contrib import admin

# Register your models here.
from .models import Position, Player

admin.site.register(Position)
# admin.site.register(Player)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_positions', 'favorite_ice_cream')
    list_filter = ('name', 'position', 'favorite_ice_cream')


admin.site.register(Player, PlayerAdmin)
