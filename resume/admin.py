from django.contrib import admin

# Register your models here.
from .models import Company, Experience, Skill, Certification, Education, Developer

admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Developer)
