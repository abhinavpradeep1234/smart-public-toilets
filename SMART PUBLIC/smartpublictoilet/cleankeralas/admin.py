from django.contrib import admin
from .models import searchtoilets,books,reports
# Register your models here.
admin.site.register(searchtoilets)
admin.site.register(books)
admin.site.register(reports)
