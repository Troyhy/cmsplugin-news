from django.contrib import admin

from cmsplugin_news.models import News

class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('slug', 'title', 'is_published')
    list_editable = ('title', 'is_published')
    list_filter = ('is_published', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
    save_as = True
    save_on_top = True

admin.site.register(News, NewsAdmin)