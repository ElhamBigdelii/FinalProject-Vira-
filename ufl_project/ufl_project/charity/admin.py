from django.contrib import admin
from .models import Modir
from .models import Charity
from .models import ProjectType
from .models import Project
# Register your models here.

admin.site.register(Modir)
admin.site.register(Charity)
admin.site.register(ProjectType)
admin.site.register(Project)
