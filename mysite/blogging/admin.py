from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CategoryInline, ]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    exclude = ('posts',)

# admin.site.register(Post)
# admin.site.register(Category)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
