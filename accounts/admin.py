from django.contrib import admin
from .models import User, Publication, Like, Comments

# Register your models here.


admin.site.register(User)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', "created_at")

admin.site.register(Like)
admin.site.register(Comments)