from django.contrib import admin
from .models import BlogArticles
# Register your models here.


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("title", "author")
    list_per_page = 15
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    ordering = ("publish", "author")


admin.site.register(BlogArticles, BlogArticlesAdmin)  # 没有提示，但不会报错
