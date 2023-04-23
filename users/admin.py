from django.contrib import admin
from users.models import User

# Register your models here.
admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username',)
#     fields = ('')

#
# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     list_display = ('')