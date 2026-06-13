from django.contrib import admin
from . models import User,Dietitian,Dietitian_post,Feedback,Contact

# Register your models here.
admin.site.register(User)
admin.site.register(Dietitian)
admin.site.register(Dietitian_post)
admin.site.register(Feedback)
admin.site.register(Contact)
