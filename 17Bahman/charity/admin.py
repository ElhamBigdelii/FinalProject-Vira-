from django.contrib import admin
from .models import Modir
from .models import Charity
from .models import ProjectType
from .models import Project
from .models import Dastebanamdy_LD
from .models import Dastebanamdy_ch
from .models import TypeCampain
# Register your models here.

admin.site.register(Modir)
admin.site.register(Charity)
admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(Dastebanamdy_LD)
admin.site.register(Dastebanamdy_ch)
admin.site.register(TypeCampain)
