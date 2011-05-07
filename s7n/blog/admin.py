from django.db import models
from django.contrib import admin
from s7n.blog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title'] }
admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    fields = ['title', 'slug', 'body', 'user', 'group', 'pub_date', 'pub_enddate', 'category', 'tag_list']
    list_display = ('title', 'user', 'group', 'category', 'pub_date', 'updated_date')
    list_filter = ('group', 'pub_date')
    ordering = ('-pub_date',)
    search_fields = ('title', 'body_html')

    def queryset(self, request):
        if request.user.is_superuser:
            qs = self.model.objects.get_query_set()
        else:
            qs = self.model.objects.get_query_set().filter(author = request.user)

        return qs
admin.site.register(Entry, EntryAdmin)
