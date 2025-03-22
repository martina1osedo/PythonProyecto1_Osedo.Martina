from django.contrib import admin

# Register your models here.
from .models import Post 

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "estado", "fecha_publicacion"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]
    #se creo uno nuevo
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Primero, aseguramos que User no esté registrado para evitar duplicaciones
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
