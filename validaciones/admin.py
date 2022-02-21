from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register (Vat)
admin.site.register (Cost)
admin.site.register (CostQuantity)
admin.site.register (Validation)

