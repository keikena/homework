# http://127.0.0.1:8000/admin/
from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price',
                    'created_date', 'updated_date', 'auction', 'get_html_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    
    # У выделенных обьектов заменяет значение поля "торг" на "нет"
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
        
    fieldsets = (
        ('Общее', {'fields': ('user', 'title', 'description', 'image')}), 
        ('Финансы', {'fields': ('price', 'auction'), 
                     'classes': ['collapse']}), 
    )
admin.site.register(Advertisement, AdvertisementAdmin)