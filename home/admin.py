from django.contrib import admin
from . models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']
    # def my_post(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #         )
    # )