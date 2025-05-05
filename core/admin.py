from django.contrib import admin
from .models import BlogPost, Tag, Category
from .models import NarrativePrediction

admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Category)

@admin.register(NarrativePrediction)
class NarrativePredictionAdmin(admin.ModelAdmin):
    list_display = ('narrative_type', 'prediction', 'status', 'added_on')
    list_filter = ('narrative_type', 'status')
    search_fields = ('prediction', 'outcome_notes')
