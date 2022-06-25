from django.contrib import admin

from posts.models import Category, Post
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display  =  ('title','is_published','selected_categories',)
    list_editable = ('is_published',)
    search_fields = ('name','description')
    list_filter = ('is_published','categories',)

    def selected_categories(self,obj):
        html = "<ul>"
        for category in obj.categories.all():
            html += "<li>"+category.name + "</li>"
        
        html += "</ul>"
        return mark_safe(html)


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
