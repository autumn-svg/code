from django.contrib import admin
from .models import CommentResult

# Register your models here.
@admin.register(CommentResult)
class CommentResultAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'created_at')
    search_fields = ('company_name',)

    
