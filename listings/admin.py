from django.contrib import admin
from .models import Listing

from .models import Realtor

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    search_fields =('name',)

admin.site.register(Listing, ListingAdmin)

