from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

# create admin object
class MyAdminSite(admin.AdminSite):
    site_header = "MikeOsa Solutions Administration"

advanced_site = MyAdminSite(name='advance-admin')
advanced_site.register(Post)