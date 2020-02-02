from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Reader)
admin.site.register(Librarian)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Administrator)