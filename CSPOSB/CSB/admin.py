from django.contrib import admin
from .models import Course, Requirement, Degree, Fulfills, Requires

# Register your models here.
admin.site.register(Course)
admin.site.register(Requires)
admin.site.register(Requirement)
admin.site.register(Degree)
admin.site.register(Fulfills)
