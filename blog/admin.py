from django.contrib import admin
from blog.models import Post, Comment, Register

admin.site.register(Register)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
