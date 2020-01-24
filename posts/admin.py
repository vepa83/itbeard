from django.contrib import admin
from . models import Post, Category, Comment, Welcome, Menu

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Welcome)
admin.site.register(Menu)
