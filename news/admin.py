from django.contrib import admin
from .models import Post, Author, Category, PostCategory, CategorySubscriber

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rating')
    list_display_links = ('id', 'user')
    search_fields = ('rating',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id',)
    search_fields = ('category_name',)

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'category')
    list_display_links = ('id',)
    search_fields = ('post',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_author', 'post_content', 'post_name', 'post_time_in',)
    list_display_links = ('id',)
    search_fields = ('post_name',)




admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(CategorySubscriber)


# Register your models here.
