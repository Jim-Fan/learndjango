from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Fields to display in list view
    list_display = ['title', 'slug', 'author', 'publish', 'status']

    # Fields to display on right-side bar with filter values
    list_filter = ['status', 'created', 'publish', 'author']

    # Searchable fields
    search_fields = ['title', 'body']

    # Fancy but not very useful
    prepopulated_fields = {'slug': ('title',)}

    # Good to have search feature for user, but display raw ID is a strange
    raw_id_fields = ['author']

    date_hierarchy = 'publish'
    ordering = ['status', 'publish']