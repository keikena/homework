from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Поставьте галочку, если торг уместен") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"<Advertisement: Advertisement({self.id}, {self.title}, {self.price})>"
    
    class Meta():
        db_table = "advertisements"
        
    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {} </span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description="дата обновления")
    def created_update(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {} </span>', updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    