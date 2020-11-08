from django.contrib import admin
from .models import Bill, BillDetail
# Register your models here.
admin.site.register(Bill)
admin.site.register(BillDetail)