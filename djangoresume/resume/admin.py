from django.contrib import admin
from .models import Data, Skill, Language, Education, Work, Template

# Register your models here.

admin.site.register(Data)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Template)
