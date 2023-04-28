from django.contrib import admin
from . models import Post
from home.models import Contact
from .models import Category

# contact page registered
admin.site.register(Contact)

# admin.site.register(Post)

# Register your models here.


@admin.register(Post)
# register category models
@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'date']
    # def my_post(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #         )
    # )
