from django.contrib import admin
from .models import Modir
from .models import Charity
from .models import TypePost
from .models import Post
# Register your models here.

admin.site.register(Modir)
admin.site.register(Charity)
admin.site.register(TypePost)
admin.site.register(Post)
